from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(unique=True, null=False, blank=False)

    def __str__(self):
        return str(self.name)
