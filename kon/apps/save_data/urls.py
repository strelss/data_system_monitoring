from django.urls import path

from . import views

app_name = 'save_data'
urlpatterns = [
    path('', views.index, name='index_url'),
    path('save/', views.send_data, name='send_data_url'),
]

print(app_name)