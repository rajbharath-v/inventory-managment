from django.urls import path
from . import views
urlpatterns = [
    path('',views.raj,name='raj'),
    path('user/',views.userDetails,name='users')
]