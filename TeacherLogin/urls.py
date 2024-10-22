from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='teacher_login'),
    path('dashboard',views.dashboard,name='dashurl')
    
]