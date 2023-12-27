import profile
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
#--------------------------pass reset------------------------------
from django.contrib.auth import update_session_auth_hash

#---------------------------pass reset----------------------------

#----------------send mail-----------------
import uuid
from .models import *
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings

#----------------send mail---------------




# Create your views here.

#--------------------------------Forget sections------------------

def Forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email:
            user = User.objects.get(email==email)
            user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'User password changed successfully.')
            return redirect('SignIn')
        else:
            messages.error(request, 'email not matched')
    return render(request, 'Account/Forget password.html')

#-----------------------------------Forget sections------------------------------

#-----------------------------------SignUP/Registration sections------------------------------

def SignUp(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if len(password) == 0 and len(password1) == 0:
            messages.warning(request, "Input Password !!!")

             # sepica; character for the gmail setup
    
        # elif  len(password) <5 : 
        #     messages.warning(request, "Enter atleast 5 character Password !!!")
        # else:
        #     b = []
        #     if password:
        #         a = [ '@','#','$','%','&','*','^']
        #     for i in a:
        #         if i in password:
        #             b.append(i)
        #if len(b) != 0:

        else:
            if password == password1:
                if User.objects.filter(username=username).exists():
                    messages.warning(request, "Username Already Taken !!!")
                elif User.objects.filter(email=email).exists():
                    messages.warning(request, "email Already Taken !!!")
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                    email=email, password=password)
                    user.set_password(password)
                    user.save()
                    #----------------send mail---------------
                    auth_token = str(uuid.uuid4())
                    pro_obj = Profile.objects.create(user=user, auth_token=auth_token)
                    pro_obj.save()
                    send_mail_registration(email, auth_token)
                    return render(request,'Account/success.html')
                
                 # else:
            #     messages.warning(request, "Enter a spical character in password !!!")   

            
            else:
                messages.warning(request, "Password not matched !!!")   

    return render(request, 'Account/SignUp.html')

def Sign_In(request):
    return render(request, 'Account/SignIn.html')


#----------------------------SignUP sections------------------------

#---------------------------SignIn sections-----------------------------
def SignIn(request):
    if request.user.is_authenticated:
        return redirect('Home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username= username,  password=password )
        if user:
            # print(user)
            prof = profile.objects.get(user=user)
            if prof.is_verified == True:
                auth.signin(request, user)
                messages.warning(request, "User Logged in.")
                return redirect('Home')
        else:
            messages.warning(request, "Verify your account.")
        return redirect('SignUp')
    
    return render(request,'Account/SignIn.html', locals())

#----------------------------------------------SignIn sections-========================

#---------------------------------------SignOut sections-------------------------------
def sign_out(request):
    auth.logout(request)
    return redirect('SignIn')

#-------------------------------------SignOut sections----------------------------------

def success(request):
    return render (request, 'success.html')


def fail(request):
    return render (request, 'fail.html')




def send_mail_registration(email, token):
    subject = "Click the link to verify your account"
    message = f'hi click the link for verify http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)



def verify(request, auth_token):
    profile_obj = Profile.objects.filter(auth_token=auth_token).first()
    profile_obj.is_verified = True
    profile_obj.save()
    messages.success(request, 'OWWO,your mail is verified')
    # print(auth_token)
    return redirect('SignIn')



























