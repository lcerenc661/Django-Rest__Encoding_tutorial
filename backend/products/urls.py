from django.urls import path 
from products import views

urlpatterns = [
    # path('', views.ProductCreateAPIView.as_view()),
    path('', views.ProductMixinView.as_view()),
    path('<int:pk>/', views.ProductMixinView.as_view()),
    path('<int:pk>/update/', views.ProductMixinView.as_view()),
    path('<int:pk>/delete/', views.ProductMixinView.as_view()),
]
