from django.contrib import admin
from django.contrib import admin
from .models import User, UserConfirmation


# Register your models here.

class UserAdminModel(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'phone_number']


class UserConfirmationModel(admin.ModelAdmin):
    list_display = []



admin.site.register(User, UserAdminModel)
admin.site.register(UserConfirmation)



