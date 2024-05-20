from uuid import uuid4
from pytils.translit import slugify

def unique_slugify(instance, slug):
    """ Генератор уникальных slug если уже имеются одноимённые """
    model = instance.__class__
    unique_slug= slugify(slug)
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}_{uuid4().hex[:8]}'
    return unique_slug