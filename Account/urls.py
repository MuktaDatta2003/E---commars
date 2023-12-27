from django.urls import path
from .views import SignIn,SignUp,Forget_password,sign_out,fail,success,verify

urlpatterns = [
    path('SignIn/', SignIn, name='SignIn'),
    path('SignUp/', SignUp, name='SignUp'),
    path('sign_out/', sign_out, name='sign_out'),
    path('success/', success, name='success'),
    path('fail/', fail, name='fail'),
    path('verify/<auth_token>/',verify, name='verify'),
    path('Forget_password/', Forget_password, name='Forget_password'),

    
]