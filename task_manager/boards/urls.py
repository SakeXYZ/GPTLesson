from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListView.as_view(), name='board_list'),
    path('board/<int:pk>/', views.BoardDetailView.as_view(), name='board_detail'),
]
