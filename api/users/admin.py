from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('bio','profile_picture')

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('bio','profile_picture')}),
    )


