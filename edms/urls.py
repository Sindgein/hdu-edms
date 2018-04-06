from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.edms, name='edms'),
    # path('f', views.file_download, name='download'),
    path('api/get_teach_file_list/', views.api_get_teach_file_list),
    path('api/get_teach_file_detail/<course_id>/',
         views.api_get_teach_file_detail),
    path('api/get_gradesign_file_list/', views.api_get_gradesign_file_list),
    path('api/get_gradesign_file_detail/<mark>/',
         views.api_get_gradesign_file_detail),
    path('api/get_student_list/', views.api_get_student_list),
    path('api/create_teach_file/', views.api_create_teach_file),
    path('api/create_gradesign_file/', views.api_create_gradesign_file),
    path('api/create_student/', views.api_creat_student),
    path('api/single_upload/<file_type>/<file_id>/<file_name>/',
         views.api_upload_single),
    path('api/file_download/<file_url>/<file_name>/', views.file_download)
]
