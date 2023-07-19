
from django.urls import path
from .views import home,delete,update

urlpatterns = [
    path('', home ,name="home"),
    # path('about', about ,name="about"),
    path('delete/<int:id>',delete,name="delete"),
    path('update/<int:id>',update,name="update"),
]
