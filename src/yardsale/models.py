from django.db import models

from django_classified.models import Item


class Reservation(models.Model):
    email = models.EmailField()
    item = models.OneToOneField(
        Item,
        related_name='reservation',
        on_delete=models.CASCADE
    )
    state = models.CharField(
        max_length=255,
        choices=(
            ('NEW', 'NEW'),
            ('PROCESSED', 'PROCESSED'),
            ('INVALIDATED', 'INVALIDATED'),
        )
    )
    inserted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} for {}'.format(self.email, self.item)
