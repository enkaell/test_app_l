from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.start, name = 'start'),
    path('lk', views.lk, name = 'lk'),
    path('lk/<int:pk>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('lk/<int:pk>/update', views.PostUpdateView.as_view(), name = 'post_update'),
    path('lk/<int:pk>/delete', views.PostDeleteView.as_view(), name='post_delete'),
]