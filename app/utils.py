from django.utils.text import slugify
from django.utils.crypto import get_random_string
import uuid


def generate_new_slug(klass,title):
    slug = slugify(title)
    qs = klass.objects.filter(slug=slug)
    if qs.exists():
        random_string = str(uuid.uuid4()).split("-")[0]
        new_slug = slug+f"-{random_string}"
        return new_slug
    return slug

