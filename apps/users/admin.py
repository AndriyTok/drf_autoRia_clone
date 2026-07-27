from django.contrib import admin
from apps.users.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff', 'created_at')
    search_fields = ('email',)
