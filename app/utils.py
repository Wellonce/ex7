import uuid

from django.utils import timezone


def avatar_path(instance, filename):
    current_dt = timezone.now()
    return f'author_photos/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'

def image_path(instance, filename):
    current_dt = timezone.now()
    return f'product_photos/{current_dt.strftime("%Y_%m")}/{uuid.uuid4().hex}/{filename}'