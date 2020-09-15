from django.contrib import admin
from .models import PlaceType,PlaceInformation,PlaceLine,CheckedUser
# Register your models here.

class PlaceAdmin(admin.ModelAdmin):
    list_display=(
        'placeId','placeName','placeLongitude','placeLatitude','owner','placeLine'
    )

class PlaceLineAdmin(admin.ModelAdmin):
    list_display=(
        'lineId','lineStatus'
    )

class CheckedUserAdmin(admin.ModelAdmin):
    list_display=(
        'checkedId','user'
    )

admin.site.register(PlaceType)
admin.site.register(PlaceInformation,PlaceAdmin)
admin.site.register(PlaceLine,PlaceLineAdmin)
admin.site.register(CheckedUser,CheckedUserAdmin)
