from django.contrib import admin
from django.shortcuts import reverse
from django.utils.html import mark_safe

from yardsale.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'item_area',
        'item_url',
        'item_price',
        'state',
        'inserted_at',
    )
    list_display_links = ('email', )
    readonly_fields = ('inserted_at', )
    list_filter = ('state', 'item__area')
    search_fields = ('email', )

    def item_url(self, obj):
        return mark_safe('<a href="{}">{}</a>'.format(
            reverse(
                'admin:{}_{}_change'.format(
                    obj.item._meta.app_label,
                    obj.item._meta.model_name
                ),
                args=(obj.item.id,)
            ),
            obj.item
        ))

    def item_price(self, obj):
        return obj.item.price

    def item_area(self, obj):
        return obj.item.area


admin.site.register(Reservation, ReservationAdmin)
