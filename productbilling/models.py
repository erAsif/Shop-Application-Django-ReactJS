import uuid
from django.db import models
from inventorymanagement.models import Category,Inventory
from django.db.models import Sum


# Create your models here.
class InvoiceModel(models.Model):
    SERVICES = (
        ('offline_shopping','offline_shopping'),
        ('home_dilivary','home_dilivary'),
    )
    customer_id = models.CharField(primary_key=True ,max_length=50) 
    services = models.CharField(max_length=20, choices=SERVICES)
    # category = models.ForeignKey(Category , on_delete=models.CASCADE )
    # inventory = models.ForeignKey(Inventory , on_delete=models.CASCADE )
    # pquantity = models.IntegerField()
    # pquantity_unit = models.CharField(max_length=50)
    # pprice = models.IntegerField(default=0)
    customer_name = models.CharField(max_length=50)
    total_purchage = models.IntegerField(default=0)
    created_at = models.DateField(auto_now=True)
    # invoice_no = models.UUIDField( default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.customer_name
    
    

class PaymentModel(models.Model):
    PAYMENT_METHOD = (
        ('CASH','cash'),
        ('DEBIT_CARD','debit_card'),
        ('CREADIT_CARD','creadit_card')
    )
    PAYMENT_STETUS = (
        ('success','success'),
        ('pending','pending'),
    )
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    payment_stetus = models.CharField(max_length=20, choices=PAYMENT_STETUS)
    customer_id = models.ForeignKey(InvoiceModel , related_name="payment_data" ,on_delete=models.CASCADE )
    product_quantity = models.IntegerField()
    product_quantity_unit = models.CharField(max_length=50)
    product_category = models.ForeignKey(Category , on_delete=models.CASCADE )
    product_name = models.ForeignKey(Inventory , on_delete=models.CASCADE )
    product_amount_pay = models.IntegerField(default=0)
    # total = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.customer_id.total_purchage += self.product_amount_pay
        self.customer_id.save()
        super(PaymentModel, self).save(*args, **kwargs)
    # def save(self, *args, **kwargs):
        # self.total += self.invoice.total_sell
        # self.save()
        # super(PaymentModel, self).save(*args, **kwargs)

class FinancialModel(models.Model):
    financial_name = models.CharField(max_length=50)

    financial_amount = models.IntegerField(default=0)
    invoice = models.ForeignKey(InvoiceModel , related_name="finacial1_data" ,on_delete=models.CASCADE )
    payment = models.ForeignKey(PaymentModel , related_name="finacial2_data" ,on_delete=models.CASCADE )
    financialdate = models.DateField(auto_now_add=True)

    # def __str__(self):
        # return self.financialtype

    def save(self, *args, **kwargs):
        self.financial_amount = InvoiceModel.total_sell 
        self.save()
        super(FinancialModel, self).save(*args, **kwargs)