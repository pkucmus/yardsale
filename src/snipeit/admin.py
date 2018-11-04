from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path
from django_classified.admin import ItemAdmin
from django_classified.models import Item, Section, Area, Group

from service.providers import snipeit


class SnipeItItemAdmin(ItemAdmin):
    change_list_template = 'snipeit/import_from_snipeit.html'

    def get_urls(self):
        urls = super().get_urls()
        snipeit_urls = [
            path(
                'import_from_snipeit/',
                self.import_from_snipeit,
                name='import-from-snipeit'
            )
        ]
        return snipeit_urls + urls

    def get_snipeit_asset_description(self, asset_data):
        return (
            'Manufacturer: {}  '
            'Model: {}  '
        ).format(
            asset_data['manufacturer']['name'],
            asset_data['model']['name']
        )

    def import_from_snipeit(self, request):
        data = snipeit.endpoints.list_hardware({'status_id': 5})
        section, __ = Section.objects.get_or_create(title='IT')
        created_count = 0
        already_staged_count = 0
        for asset_data in data['rows']:
            item, created = Item.objects.get_or_create(
                slug='snipeit_asset_{}'.format(asset_data['asset_tag']),
                defaults={
                    'user': request.user,
                    'area': Area.objects.get_or_create(
                        title=asset_data['location']['name']
                    )[0],
                    'group': Group.objects.get_or_create(
                        title=asset_data['category']['name'],
                        defaults={
                            'section': section,
                        }
                    )[0],
                    'title': asset_data['model']['name'],
                    'description': self.get_snipeit_asset_description(
                        asset_data
                    ),
                    'price': 10000.00,
                    'is_active': False,
                }
            )
            if created:
                created_count += 1
            else:
                already_staged_count += 1
        self.message_user(
            request,
            (
                'Imported {} hardware assets, '
                '{} assets were already staged. '
                'Total from SnipeIt was {}.'
            ).format(created_count, already_staged_count, data['total'])
        )
        return HttpResponseRedirect('../')


admin.site.unregister(Item)
admin.site.register(Item, SnipeItItemAdmin)
