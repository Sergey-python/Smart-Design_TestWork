from django.db import models
from jsonfield import JSONField


class Product(models.Model):

    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание', null=True, blank=True)
    parameters = JSONField('Параметры', default=dict)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'
        ordering = ['title']