from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=500, default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')

    def __str__(self) -> str:
        return f'Item_name is:{self.item_name} and the price is {self.item_price}'

    def get_absolute_url(self):
        return reverse("food:detailview", kwargs={"pk": self.pk})
