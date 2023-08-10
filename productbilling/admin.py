from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(InvoiceModel)
admin.site.register(PaymentModel)
admin.site.register(FinancialModel)
