from django.shortcuts import render
from django.views import View


class DashboardPage(View):
    def get(self, request):
        return render(request, 'dashboard.html')


class TablesPage(View):
    def get(self, request):
        return render(request, 'tables.html')



class BillingPage(View):
    def get(self, request):
        return render(request, 'billing.html')


class VirtualReality(View):
    def get(self, request):
        return render(request, 'virtual-reality.html')


class RtlPage(View):
    def get(self, request):
        return render(request, 'rtl.html')


class NotificationsPage(View):
    def get(self, request):
        return render(request, 'notifications.html')