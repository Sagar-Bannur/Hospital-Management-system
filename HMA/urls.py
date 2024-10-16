from django.urls import path
from HMA import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('patients/', views.patients, name='patients'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointments/', views.appointments, name='appointments'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('add_appointment/', views.add_appointment, name='add_appointment'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('update_patient/<int:pk>/', views.update_patient, name='update_patient'),
    path('delete_patient/<int:pk>/', views.delete_patient, name='delete_patient'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
