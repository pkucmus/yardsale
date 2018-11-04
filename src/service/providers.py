from django.conf import settings
from snipeit.client import SnipeItClient


snipeit = SnipeItClient(
    settings.SNIPEIT_URL,
    settings.SNIPEIT_API_JWT,
    verify_https=settings.SNIPEIT_HTTPS_VERIFY
)
