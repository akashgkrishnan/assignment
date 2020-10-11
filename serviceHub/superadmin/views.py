from django.shortcuts import render, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm
from .decorator import allowed_users, unauthenticated_user
from service_user.models import service_user_details
from client_user.models import client_user_details

@login_required(login_url='login')
def home(request):
    print('hi')
    group = request.user.groups.all()[0].name
    if group == 'service_provider':
        return redirect('service_home')

    elif group == 'client_user':
        return redirect('client_home')

    else:
        return redirect('superadmin_register')


@unauthenticated_user
def login_view(request):
    context = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password not right')

    return render(request, 'superadmin/login.html', context)


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['super_admin'])
def register_view(request):
    form = UserRegisterForm()
    groups = Group.objects.all()

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'{user} added')

            user_group = request.POST.get('group_name')
            
            if user_group == 'client_user':
                temp_user = User.objects.get(username=user)
                new_service_temp = client_user_details(user_info=temp_user)
                new_service_temp.save()
            else:
                temp_user = User.objects.get(username=user)
                new_service_temp = service_user_details(user_info=temp_user)
                new_service_temp.save()

            group = Group.objects.get(name=user_group)
            new_user.groups.add(group)
            return redirect('superadmin_register')

    context = {
        'form': form,
        'groups': groups
    }
    return render(request, 'superadmin/superadmin_register.html', context)


def not_auth_user(request):
    return render(request, 'superadmin/not_auth.html', {})
