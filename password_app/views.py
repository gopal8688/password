from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Registration
from .forms import RegistrationForm
from django.core.mail import send_mail
from password_reset import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    register = Registration.objects.all()
    return render(request, 'home.html', {'register': register})


def Register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email = cd['email']
            a = Registration.objects.filter(email=email)
            print(not a)
            if not a:
                form.save()
                url = request.build_absolute_uri(form.get_absolute_url())
                subject = "{}saved".format(cd['username'])
                message = "{}login here".format(url)
                send_mail(subject, message, settings.EMAIL_HOST_USER, [cd['email']])
                messages.success(request, 'data is saved')
                return redirect('Register')
            else:
                messages.error(request, 'email already existed')
                return redirect('Register')

        else:
            messages.error(request, 'something went wrong')
            return redirect('Register')
    else:
        form = RegistrationForm()
        return render(request, 'Register.html', {'form': form})


def log_in(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        reg = Registration.objects.get(email=email, password=password)
        if reg:
            return render(request, 'welcome.html', {'reg': reg.username})
        else:
            return redirect('log_in')
    else:
        return render(request, 'log_in.html')


import random


def forget_password(request):
    if request.method == "POST":
        email = request.POST['email']

        b = Registration.objects.filter(email=email)
        if b:
            otp = random.randint(5000, 9999)
            b.update(password=otp)
            subject = 'password'
            message = '{}this is the one time otp'.format(str(otp))
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email, ])
            return render(request, 'otp_verify.html', {'msg': 'otp send to your mail'})
        else:
            messages.error(request, 'otp is invalid,send otp again')
            return redirect('forget_password')
    else:
        return render(request, 'otp.html')


def new_password(request):
    password = request.POST['password']
    password1 = request.POST['password1']
    if password == password1:
        d = Registration.objects.filter(id=request.GET['id'])
        d.update(password=password)
        messages.success(request, 'password succesfully changed')
        return redirect('log_in')
    else:
        return None


def verify_otp(request):
    otp = request.POST['otp']
    print(otp, type(otp))
    c = Registration.objects.get(password=otp)
    if c:
        return render(request, 'new_password.html', {'c': c})
    else:
        messages.error(request, 'invalid OTP')
        return redirect('forget_password')


def search(request):
    return HttpResponse('No data implemeted')


def contact_details(request):
    return HttpResponse('No data implemeted')


def about_project(request):
    return HttpResponse('No data implemeted')
