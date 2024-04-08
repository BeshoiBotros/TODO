from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoItemView.as_view()),
    path('<int:pk>/', views.TodoItemView.as_view()),
]
