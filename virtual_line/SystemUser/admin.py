from django.contrib import admin
from .models import UserPermission,UserType,SystemUser

class SystemUserAdmin(admin.ModelAdmin):
    list_display=(
        'userId','name','phoneNumber'
    )
# Register your models here.

admin.site.register(UserPermission)
admin.site.register(UserType)
admin.site.register(SystemUser,SystemUserAdmin)
