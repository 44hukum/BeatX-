from django.urls import path
from . import views
app_name='Registration'
urlpatterns=[
    path('',views.index,name='index'),
    path('beatxuserlogin/',views.login,name='login'),
    path('beatxusersignup/',views.signup,name='signup'),
    path('forgetpassword/',views.forgetpass,name='forgetpass'),
    path('beatX_logout/',views.logout,name='logout'),
    path('deleteUser/',views.deleteUser,name='deleteUser'),
]
