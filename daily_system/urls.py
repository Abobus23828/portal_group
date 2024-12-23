from django.urls import path
from . import views

urlpatterns = [
    path('', views.LessonsListView.as_view(), name='daily'),
    path('homework/<int:pk>/', views.HomeworkDetailView.as_view(), name='homework-detail'),
]