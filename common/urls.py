from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'common'

urlpatterns=[
    #path('login/', auth_views.LoginView.as_view(), name='login')
    path('login/', auth_views.LoginView.as_view(
        template_name = 'common/login.html' 
        #registration/login.html 대신 templates/common/login.html을 참조하기 위함
    ), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name="signup")
]
