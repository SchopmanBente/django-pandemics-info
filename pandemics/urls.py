from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('who', views.who_coronavirus_update, name="WHO update")
]