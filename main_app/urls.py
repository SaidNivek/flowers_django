from django.urls import path
from . import views

# this like app.use() in express
urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('flowers/', views.FlowerList.as_view(), name="flower_list"),
    path('flowers/new/', views.FlowerCreate.as_view(), name="flower_create"),
    path('flowers/<int:pk>/', views.FlowerDetail.as_view(), name="flower_detail"),
    path('flowers/<int:pk>/update', views.FlowerUpdate.as_view(), name="flower_update"),
    path('flowers/<int:pk>/delete', views.FlowerDelete.as_view(), name="flower_delete"),
]