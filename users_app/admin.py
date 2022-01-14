from django.contrib import admin
from .models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name',
                    'phone_number']
    fieldsets = (
        ('General Info', {
            'fields': ('username', 'email', 'phone_number')
        }),

        ('Details', {
            'fields': ('first_name', 'last_name', 'birth_day', 'last_login', 'date_joined', 'password',)
        }),

        ('Account_permissions', {
            'classes': ('collapse',),
            'fields': ('is_superuser', 'is_staff', 'is_active', 'terms_and_conditions',
                       'groups', 'user_permissions')
        }),
    )

