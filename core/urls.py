from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [
    path('api/v1/', include('customers.urls')),
    path('api/v1/', include('parking.urls')),
    path('api/v1/', include('vehicles.urls')),
    path('api/v1/', include('authentication.urls')),
    path('', admin.site.urls),
]
