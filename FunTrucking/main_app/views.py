# main_app/views.py

# views.py

class Truck:
    def __init__(self, name, make, description, year):
        self.name = name
        self.make = make
        self.description = description
        self.year = year

# Create a list of Cat instances
trucks = [
    Truck('Titan', 'Ford', 'Heavy-duty off-road truck.', 2020),
    Truck('Ranger', 'Toyota', 'Compact and fuel-efficient.', 2023),
    Truck('Silverado', 'Chevrolet', 'Luxury pickup with advanced features.', 2019),
    Truck('Rebel', 'Ram', 'Powerful engine, suitable for towing.', 2017)

]

from django.shortcuts import render , redirect
from .models import Truck
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import fueltypeForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class Home(LoginView):
    template_name = 'home.html'

# Define the about view function

def about(request):
    return render(request, 'about.html')

@login_required
def truck_index(request):
    trucks = Truck.objects.filter(user=request.user)
    return render(request, 'trucks/index.html', { 'trucks': trucks })   

def truck_detail(request, truck_id):
    truck = Truck.objects.get(id=truck_id)
    fueltype_form = fueltypeForm()
    return render(request, 'trucks/detail.html', { 'truck': truck, 'fueltype_form': fueltype_form })

class TruckCreate(LoginRequiredMixin,CreateView):
    model = Truck
    fields = ['make', 'description', 'year']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TruckUpdate(UpdateView):
    model = Truck
    fields = ['make', 'description', 'year']

class TruckDelete(DeleteView):
    model = Truck
    success_url = '/trucks/'

def add_fuel(request, truck_id):
    form = fueltypeForm(request.POST)
    if form.is_valid():
        new_fuel = form.save(commit=False)
        new_fuel.truck_id = truck_id
        new_fuel.save()
    return redirect('truck-detail', truck_id=truck_id)


def signup (request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('truck-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)