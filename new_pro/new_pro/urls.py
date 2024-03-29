
from django.contrib import admin
from django.urls import path
from shorten.views import index,create,goto,update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index,name="index"),
    path('add/', create,name="create"),
    path('<str:shortcode>/', goto,name="redirect"),
    path('edit/<int:id>/',update,name="update"),
    path('delete/<int:id>/',delete,name="delete"),
]
