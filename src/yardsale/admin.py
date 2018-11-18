from django.contrib import admin

from yardsale.models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('email', 'item', 'state', 'inserted_at', )
    list_display_links = ('email', )
    readonly_fields = ('inserted_at', )
    list_filter = ('state', )
    search_fields = ('email', )


admin.site.register(Reservation, ReservationAdmin)
