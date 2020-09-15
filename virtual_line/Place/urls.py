from django.urls import path
from .views import addPlace,getAllPlace,getPlaceType,getPlaceByOwner,getPlaceById,changeLineStatus,removeUserFromLine,addUserInLine

urlpatterns =[
    path('add_place/',addPlace,name='add_place'),
    path('get_all_place/',getAllPlace,name='get_all_place'),
    path('get_place_type/',getPlaceType,name='get_place_type'),
    path('get_place_by_owner/',getPlaceByOwner,name='get_place_by_owner'),
    path('get_place_by_id/',getPlaceById,name="get_place_by_owner"),
    path('change_line_status/',changeLineStatus,name="change_line_status"),
    path('remove_user_from_line/',removeUserFromLine,name="remove_user_from_line"),
    path('add_user_in_line/',addUserInLine,name="add_user_in_line")
]