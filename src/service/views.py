from django.core.mail import EmailMessage, BadHeaderError
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django_classified.views import ItemDetailView
from django_classified.models import Item


from service.forms import ContactForm


class ItemDetailView(ItemDetailView):
    form = ContactForm()
    model = Item
    queryset = Item.active

    def get_form(self, request=None):
        if request:
            return ContactForm(request)
        return self.form

    def get_context_data(self, **kwargs):
        form = self.get_form()
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
        form = self.get_form(request.POST)
        instance = self.get_object()

        if form.is_valid():
            from_email = form.cleaned_data['from_email']
            message = '{}\nItem url: {}'.format(
                form.cleaned_data['message'],
                request.get_raw_uri()
            )
            subject = form.cleaned_data['subject']
            to_email = instance.user.email

            try:
                mail = EmailMessage(
                    subject=subject,
                    body=message,
                    from_email=settings.EMAIL_FROM,
                    to=[to_email],
                    reply_to=[from_email],
                )
                mail.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

        return redirect(instance.get_absolute_url())
