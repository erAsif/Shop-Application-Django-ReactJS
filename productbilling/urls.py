from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('invoice', views.InvoiceView , basename="invoice")
router.register('payment', views.PaymentView , basename="payment")
router.register('customerstatement', views.CustomerStatementView , basename="customerstatement")
router.register('servicereport', views.ServiceReportView , basename="servicereport")
router.register('financialreport', views.FinancialView , basename="financialreport")


urlpatterns = [
    path("",include(router.urls)),
]