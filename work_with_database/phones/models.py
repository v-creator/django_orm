from django.db import models


class Phone(models.Model):
    name = models.TextField()
    price = models.TextField()
    image = models.TextField()
    release_date = models.TextField()
    lte_exists = models.TextField()
    slug = models.SlugField()
