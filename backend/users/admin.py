from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, StudentProfile, RecruiterProfile, CoordinatorProfile

class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )

admin.site.register(User, UserAdmin)
admin.site.register(StudentProfile)
admin.site.register(RecruiterProfile)
admin.site.register(CoordinatorProfile)
