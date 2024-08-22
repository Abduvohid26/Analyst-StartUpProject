from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('dashboard/', views.DashboardPage.as_view(), name='dashboard'),
    path('tables/', views.TablesPage.as_view(), name='tables'),
    path('billing/', views.BillingPage.as_view(), name='billing'),
    path('virtual-reality/', views.VirtualReality.as_view(), name= 'virtual-reality'),
    path('rtl/', views.RtlPage.as_view(), name = 'rtl'),
    path('notifications/', views.NotificationsPage.as_view(), name = 'notifications')
]