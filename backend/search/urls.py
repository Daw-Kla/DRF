from django.urls import path

from . import views

urlpatterns = [
    path('', views.SearchlistView.as_view(), name='search')
]