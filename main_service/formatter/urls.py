from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_text, name='create_text'),
    path('edit/<int:text_id>/', views.edit_text, name='edit_text'),
    path('delete/<int:text_id>/', views.delete_text, name='delete_text'),
    path('api/texts/', views.text_list_api, name='text_list_api'),
]