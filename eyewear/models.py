from django.db import models

# Create your models here.

class Glasses(models.Model):
    frame_name = models.TextField(max_length=200)
    brand = models.TextField(max_length=200, default='')
    product_group_type = models.TextField(max_length=200, default='')
    frame_color_type = models.TextField(max_length=200, default='')
    gender_type = models.TextField(max_length=200, default='')
    material_type=models.TextField(max_length=200, default='')


    def __str__(self):
        return self.frame_name


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    def __str__(self):
        summary = self.name + " " + self.description + " $" + str(self.price)
        return summary


class Cart2(models.Model):
    owner = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    cart = models.ForeignKey(Cart2, related_name="cart_items")
    item = models.ForeignKey(Item)

    def __str__(self):
        summary = self.cart.name + " " + self.item.name
        return summary


# class Cart(models.Model):
#     item = models.CharField(max_length=200, unique=True)
#     def __str__(self):
#         return self.item
