from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import NewCarCreateView, CarsListView, CarDetailView, CarUpdateView, CarDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarsListView.as_view(), name='home'),  # Home page showing the list of cars
    path('register/', register_view, name='register'),  # Page for user registration
    path('login', login_view, name='login'),  # Login view
    path('logout/', logout_view, name='logout'),  # Redirect to the home page after logout
    path('cars/', CarsListView.as_view(), name='cars_list'), # List of cars
    path('new_car/', NewCarCreateView.as_view(), name='new_car'),  # Page to add a new car
    path('car/<int:pk>/', CarDetailView.as_view(), name='car_detail'),  # Detail view for a specific car
    path('car/<int:pk>/update/', CarUpdateView.as_view(), name='car_update'),  # Update view for a specific car
    path('car/<int:pk>/delete/', CarDeleteView.as_view(), name='car_delete'),  # Delete view for a specific car
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
