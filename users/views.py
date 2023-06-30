from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .forms import LoginForm, RegisterForm

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string, get_template
from django.template import Context
from django.utils.html import strip_tags

# Create your views here.


def sign_up(request):

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            # mail system
            html = get_template('users/email_template.html')
            context = {'username': user.username}
            subject, from_email, to = 'Welcome', 'narrativehub2.0@gmail.com', user.email
            html_content = html.render(context)
            message = EmailMultiAlternatives(
                subject, html_content, from_email, [to])
            message.attach_alternative(html_content, 'text.html')
            message.send()
            # messages.success(
            #     request, 'Thank you for signing up in Narrative Hub')
            login(request, user)
            return redirect("storyposts")
        else:
            return render(request, 'users/register.html', {'form': form})


def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('storyposts')
        form = LoginForm()
        return render(request, 'users/login.html', {"form": form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f'Hi {username.title()}, welcome back!')
                return redirect("storyposts")

        messages.error(request, f'Invalid username or password')
        return render(request, 'users/login.html', {'form': form})


def sign_out(request):
    logout(request)
    messages.success(request, f"You have been logged out.")
    return redirect('login')
