# This connects a URL path to the view.
from django.urls import path

from . import views  # ← This means: use functions from views.py in the same folder

urlpatterns = [
    path('', views.calculator, name='home'),
    path('calculator/', views.calculator, name='calculator'),
    
]
