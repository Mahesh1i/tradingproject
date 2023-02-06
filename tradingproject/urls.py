from mainapp import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mainapp/', views.upload_csv, name = 'mainapp'),
    path('download_json/', views.download_json, name = 'download_json'),
]
