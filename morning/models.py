from django.db import models


# Create your models here.
class Clothing(models.Model):
    sleeve = models.CharField(max_length=10)
    thick = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    brand = models.CharField(max_length=20)

    class Meta:
        verbose_name = verbose_name_plural = '衣服'

    def __str__(self):
        return self.brand