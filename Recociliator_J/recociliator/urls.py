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
    
    # Form yes input page
    path('split-yes/', views.split_yes_input, name='split_yes_input'),
    
    # Result yes calculation page
    path('split-yes/result/', views.split_yes_result_view, name='split_yes_result'),
]
