from django.db import models


# Create your models here.

class House(models.Model):
    active = models.BooleanField("активний", default=True)
    name = models.CharField("назва", max_length=50)
    price = models.IntegerField("ціна")
    description = models.TextField("опис")
    photo = models.ImageField("фотографія", upload_to="houses/photo", default="", blank=True)
    class Meta:
        verbose_name = "будинок"
        verbose_name_plural = "будинки"
        ordering = ["-active", "name"]


    def __str__(self):
        return self.name