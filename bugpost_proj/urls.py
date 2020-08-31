"""bugpost_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from bugpostapp.views import login_view, logout_view
from homepage import views
urlpatterns = [
    path('', views.index, name='homepage'),
    path('create_ticket_view/', views.create_ticket_view),
    path('ticket/<int:ticket_id>/edit/', views.ticket_edit_view),
    path('ticket/<int:ticket_id>/', views.ticket_detail_view),
    path('in_progress_ticket_view/<int:ticket_id>/', views.in_progress_ticket_view),
    path('completed_ticket_view/<int:ticket_id>/', views.completed_ticket_view),
    path('invalid_ticket_view/<int:ticket_id>/', views.invalid_ticket_view),
    path('user_detail_view/<int:ticket_id>/', views.user_detail_view),
    path('login/', login_view, name='loginview'),
    path('logout/', logout_view, name="logoutview"),
    path('admin/', admin.site.urls),
]
