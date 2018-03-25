from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.edms, name='edms'),
    # path('f', views.file_download, name='download'),
    path('api/',views.get_teachfile,name='teachfileinfo')
]
