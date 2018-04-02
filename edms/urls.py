from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.edms, name='edms'),
    # path('f', views.file_download, name='download'),
    path('api/get_teach_file_list/', views.get_teach_file_list),
    path('api/get_teach_file_detail/<course_id>/', views.get_teach_file_detail),
    path('api/get_gradesign_file_list/',views.get_gradesign_file_list),
    path('api/get_gradesign_file_detail/<graduation_thesis>/',views.get_gradesign_file_detail),
    path('api/create_teach_file/',views.api_create_teach_file)
]
