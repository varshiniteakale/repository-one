from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
import random
from .models import Advertisements
# Create your views here.


def index(request):
    obje = Advertisements.objects.all()
    return render(request, 'index.html', {'data': obje})


def login_page(request):
    if(request.method == "POST"):
        uname = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)
            get_data = User.objects.get(username=uname)
            global x
            x = get_data
            return render(request, 'user_page.html', {'info': get_data})
        else:
            return render(request, 'error_page.html')
    else:
        return render(request, 'login_page.html')


num1 = random.randint(0, 100)


def one():
    num2 = random.randint(0, 50)
    if(num1 != num2):
        return num2
    else:
        one()


def register_form(request):
    if(request.method == "POST"):
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        uname = fname + str(num1)
        if(password1 == password2):
            if User.objects.filter(username=uname).exists():
                num2 = one()
                uname = fname + str(num2)
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email Taken")
            else:
                user = User.objects.create_user(
                    username=uname, password=password1, email=email, first_name=fname, last_name=lname)
                user.save()
                return render(request, 'login_success_page.html', {'info': uname})
        else:
            return HttpResponse("Password Mismatch")


def advertisements_page(request):
    adv_title = request.POST['title']
    adv_subject = request.POST['subject']
    adv_image = request.FILES["adv-image"]

    advertisement_obj = Advertisements(
        advertisement_title=adv_title, advertisement_subject=adv_subject, advertisement_image=adv_image)
    advertisement_obj.save()

    return render(request, 'success_page.html')


def user_page(request):
    return render(request, 'user_page.html', {'info': x})


def logout(request):
    auth.logout(request)
    return redirect('/')
