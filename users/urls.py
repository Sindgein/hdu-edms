from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    re_path(r'^active/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$',
            views.active, name='active_user')
]
