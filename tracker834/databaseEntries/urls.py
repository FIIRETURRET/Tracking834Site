from django.urls import path

from . import views

app_name = 'databases'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:database_id>/', views.detail, name='detail'),
    path('new_database/', views.new_database, name='new_database')
]