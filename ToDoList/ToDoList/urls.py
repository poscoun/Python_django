from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('my_to_do_app.urls')),
    path('admin/', admin.site.urls),
]