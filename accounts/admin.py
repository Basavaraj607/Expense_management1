from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "role", "get_manager", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Role & Manager", {"fields": ("role", "manager")}),
    )

    def get_manager(self, obj):
        return obj.manager.get_full_name() if obj.manager else "-"
    get_manager.short_description = "Manager"
    get_manager.admin_order_field = "manager"

admin.site.register(User, CustomUserAdmin)
