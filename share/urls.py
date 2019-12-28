from django.contrib import admin
from django.urls import path
from .views import image_list_view,display_images,image_detail,image_edit

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('admin/', admin.site.urls),
    path('',image_list_view,name='images'),
    path('list',display_images,name="displayimage"),
    path('image/<int:pk>',image_detail,name="detailimage"),
    path('image/<int:pk>/edit',image_edit,name="editimage")
]