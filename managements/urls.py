from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.res_add, name='res_add'),
    path('list/', views.res_list, name='res_list'),
    path('update/<int:res_id>/', views.res_update, name='res_update'),
    path('delete/<int:res_id>/', views.res_delete, name='res_delete'),
    
    path('add_f/<int:resf_id>/', views.resf_add, name='resf_add'),
    path('list_f/<int:res_id>/', views.resf_list, name='resf_list'),
    path('delete_f/<int:resf_id>/', views.resf_delete, name='resf_delete'),
    
]