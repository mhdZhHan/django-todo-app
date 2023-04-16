from django.urls import path

from web import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('complete/<int:pk>/', views.complete_task, name='complete'),
    path('undo/<int:pk>/', views.undo_task, name='undo'),
    path('delete/<int:pk>/', views.delete_task, name='delete'),
    path('update/<int:pk>/', views.update_task, name='update'),
]