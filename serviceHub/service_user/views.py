from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import service_offered, service_booking_detail, service_user_details
from django.contrib import messages
from .forms import MyServiceForm
from superadmin.decorator import allowed_users



@login_required(login_url='login')
@allowed_users(allowed_roles=['service_provider'])
def home(request):
    form = MyServiceForm()


    if request.method == 'POST':
        form = MyServiceForm(request.POST)
        
        if form.is_valid():
            new_service = form.save(commit=False)
            user_name = User.objects.filter(username=request.user)[0]
            new_service.user_name = user_name
            messages.success(request,'service added')
            new_service.save()
        else:
            messages.error(request,form.errors)
            print('Not valid')

        return redirect('service_home')

    context = {
        'form': form
    }

    return render(request, 'service_user/service_user_home.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['service_provider'])
def requested_service(request):
    service_user = service_user_details.objects.get(user_info = request.user.id)
    services = service_booking_detail.objects.filter(service_provider = service_user)
    context = {
        'services': services
    }
    return render(request, 'service_user/service_users_requested_services.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['service_provider'])
def my_services(request):
    user = request.user
    services = service_offered.objects.filter(user_name = user)

    context = {
        'services': services
    }
    return render(request, 'service_user/service_user_my_services.html', context)