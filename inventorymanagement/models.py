from django.db import models
from model_utils import Choices


class Category(models.Model):
    category = models.CharField(max_length=50,primary_key=True)
    total_amount = models.IntegerField(default=0)

    def __str__(self):
        return self.category 

class Inventory(models.Model):
    category = models.ForeignKey(Category , related_name="inventory_data",on_delete=models.CASCADE)
    name = models.CharField(max_length=50,primary_key=True )
    quantity = models.IntegerField()
    quantity_unit = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.category.total_amount += self.price
        self.category.save()
        super(Inventory, self).save(*args, **kwargs)


class Reorder(models.Model):
    ORDER_STATUS = (
        ('order_success','order_success'),
        ('delivary_on_way','delivary_on_way'),
        ('delivary_success','delivary_success')
    )
    inventory = models.ForeignKey(Inventory , related_name="reorder_data",on_delete=models.CASCADE)
    re_order_quantity =  models.IntegerField()
    re_order_quantity_unit =  models.CharField(max_length=20)
    re_order_status  = models.CharField(max_length=20, choices=ORDER_STATUS)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.re_order_status
