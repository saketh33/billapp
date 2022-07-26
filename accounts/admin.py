from django.contrib import admin

# Register your models here.
from .models import Profile,Notifications
admin.site.register(Profile)
admin.site.register(Notifications)

class NotificationsInline(admin.StackedInline):
    model = Notifications
    extra = 1