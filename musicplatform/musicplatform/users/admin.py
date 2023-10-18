from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):

    list_display = ['username', 'first_name', 'last_name',
                    'email', 'bio', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username']


admin.site.register(User, UserAdmin)
