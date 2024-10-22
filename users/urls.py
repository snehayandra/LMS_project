from django.urls import path,include
from .views import login_view, register_view,dashboard
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login_view, name='loginurl'),             # Root URL for login page
    path('register/', register_view, name='register'), # URL for registration page
    path('dashbord/',dashboard,name='std_dashurl'),
    path('logout/', LogoutView.as_view(next_page='loginurl'), name='logout'), # URL for logging out
    path('accounts/', include('django.contrib.auth.urls')),  # Include authentication URLs
]

