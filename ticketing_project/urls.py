"""
URL configuration for ticketing_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tickets import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL
    path('create-ticket/', views.ticket_create, name='ticket_create'),
    path('success/', views.ticket_success, name='ticket_success'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('ticket-list/', views.ticket_list, name='ticket_list'),
    path('notification-center/', views.notification_center, name='notification_center'),
    path('notification-center/read/<int:notification_id>/', views.mark_as_read, name='mark_as_read'),
    path('get-ticket-count/', views.get_ticket_count, name='get_ticket_count'),

]
