from django.urls import path,include
from .views import servertest,register,login

urlpatterns = [
    # path('servertest/', servertest ,name="servertest"),

    
    # path('auth/register/', register ,name="register"),
    # path('auth/login/', login ,name="login"),
    # path('auth/', include('rest_auth.urls')),
    # path('auth/registration/', include('rest_auth.registration.urls'))
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls'))

]