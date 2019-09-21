from django.urls import path
from . import views
urlpatterns = [
    path('', views.Upload, name='Upload'),
    path('blog/Upload/', views.Upload , name='up'),
]
