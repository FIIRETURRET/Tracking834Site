from django.urls import path

from . import views

app_name = 'entries'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:query_id>/', views.detail, name='detail'),
    path('export/csv/', views.export_entries_csv, name='export_entries_csv'),
    path('upload/csv/', views.csv_upload, name='csv_upload')
]