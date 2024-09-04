from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('trucks/', views.truck_index, name='truck-index'),
    path('trucks/<int:truck_id>/', views.truck_detail, name='truck-detail'),
    path('trucks/create/', views.TruckCreate.as_view(), name='truck-create'),
    path('trucks/<int:pk>/update/', views.TruckUpdate.as_view(), name='truck-update'),
    path('trucks/<int:pk>/delete/', views.TruckDelete.as_view(), name='truck-delete'),
    path('trucks/<int:truck_id>/add_fuel/', views.add_fuel, name='add_fuel'),
    path('accounts/signup/', views.signup, name='signup'),
]