from django.urls import path

from . import views

urlpatterns = [
    # class based views
    path('', views.ProductListCreateAPIView.as_view()),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    path('<int:pk>/', views.ProductDeailAPIView.as_view())
    
    # function based views
    #path('', views.product_alt_view),
    #path('<int:pk>/', views.product_alt_view)

] 