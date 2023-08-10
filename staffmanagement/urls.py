from django.urls import path,include
from staffmanagement.views import ProfileViews,ScheduleViews,PerformanceViews
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'staff', ProfileViews )
router.register(r'schedule', ScheduleViews )
router.register(r'performance', PerformanceViews )


urlpatterns = [
    path("",include(router.urls)),
]