from django.urls import path,include
from .views import CategoryView,InventoryView,LowstockView,ReorderView,ReportView,Search
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'inventory', InventoryView )
router.register(r'category', CategoryView )
router.register(r'lowstock',LowstockView )
router.register(r'search', Search )
router.register(r'reorder', ReorderView )
router.register(r'report', ReportView )


urlpatterns = [


    path("",include(router.urls)),

]