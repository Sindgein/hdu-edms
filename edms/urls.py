from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.edms, name='edms'),
    # path('f', views.file_download, name='download'),
    path('api/get_teachfile_list/',views.get_teachfile_list),
    path('api/get_teachfile/<filename>/',views.get_teachfile)
]
