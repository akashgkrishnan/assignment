from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from superadmin.decorator import allowed_users
from service_user.models import service_offered, service_booking_detail, service_user_details
from .models import client_user_details
from django.views.decorators.http import require_POST
@login_required(login_url='login')
@allowed_users(allowed_roles=['client_user'])
def home(request):
    services = service_offered.objects.all()

    context = {
        'services': services
    }
    return render(request, 'client_user/client_user_home.html', context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['client_user'])
def book_service(request, pk):
    
    service = service_offered.objects.get(pk=pk)
    service_user = service_user_details.objects.get(user_info = service.user_name)
    client_user = client_user_details.objects.get(user_info = request.user.id)
    new_booking = service_booking_detail(service_id= service, client_booked_for= client_user, service_provider= service_user)
    new_booking.save()

    services = service_booking_detail.objects.filter(client_booked_for = client_user)
    context = {
        'services': services
    }
    return redirect('raised-sr')


@login_required(login_url='login')
@allowed_users(allowed_roles=['client_user'])
def raised_sr(request):
    client_user = client_user_details.objects.get(user_info = request.user.id)
    services = service_booking_detail.objects.filter(client_booked_for = client_user)
    context = {
        'services': services
    }
    return render(request, 'client_user/raised_sr.html', context)

