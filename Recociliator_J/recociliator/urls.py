# This connects a URL path to the view.
from django.urls import path
from . import views

urlpatterns = [
    # Home page or default calculator
    path('', views.calculator, name='home'),

    # Calculator page
    path('calculator/', views.calculator, name='calculator'),

    # Next step page
    path('next/', views.next_step, name='next_step'),
]
