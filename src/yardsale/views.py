from django.core.mail import EmailMultiAlternatives, BadHeaderError
from django.conf import settings
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader
from django.utils.html import strip_tags
from django.views.generic import TemplateView
from django_classified.views import ItemDetailView
from django_classified.models import Item

from yardsale.forms import ContactForm
from yardsale.models import Reservation


class ItemDetailView(ItemDetailView):
    model = Item
    queryset = Item.active

    def get_context_data(self, **kwargs):
        form = ContactForm()
        instance = self.get_object()

        context = super().get_context_data(**kwargs)
        message = 'Hello, i would like to buy an item: {}, id: {}'.format(
            instance.title,
            instance.id,
        )
        form.fields['message'].initial = message
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        instance = self.get_object()

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            to_email = instance.user.email

            with transaction.atomic():
                Reservation.objects.create(
                    email=from_email,
                    item=instance,
                    state='NEW'
                )
                instance.is_active = False
                instance.save()

                html_content = loader.render_to_string(
                    'emails/reservation.html',
                    {
                        'request': request,
                        'item': instance,
                        'message': form.cleaned_data['message']
                    },
                    request
                )

                try:
                    mail = EmailMultiAlternatives(
                        subject=subject,
                        body=strip_tags(html_content),
                        from_email=settings.EMAIL_FROM,
                        to=[
                            from_email
                        ],
                        cc=[
                            to_email,
                            settings.ADMIN_EMAIL,
                            settings.ACCOUNTANT_EMAIL
                        ],
                        reply_to=[from_email],
                    )
                    mail.attach_alternative(html_content, 'text/html')
                    mail.send()
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

        return redirect('reserved')


class ReservationOutcomeView(TemplateView):
    template_name = 'reservation_outcome.html'
