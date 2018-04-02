from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.account_signin, name='signin'),
    path('register/', views.account_register, name='register'),
    re_path(r'^active/(?P<token>\w+.[-_\w]*\w+.[-_\w]*\w+)/$',
            views.account_active, name='active_user')
]
