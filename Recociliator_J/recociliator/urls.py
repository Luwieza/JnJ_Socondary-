# This connects a URL path to the view.
from django.urls import path

from django.urls import path
from .views import calculator, split_number, next_step   # views.py
from .yes_views import split_yes_input, split_yes_result_view
from .no_views import split_no_input


urlpatterns = [
    # Home page or default calculator
    path('', calculator, name='home'),

    # Calculator page
    path('calculator/', calculator, name='calculator'),

    # Next step page
    path('next/', next_step, name='next_step'),
    
    # Form yes input page
    path('split-yes/', split_yes_input, name='split_yes_input'),
    
    # Result yes calculation page
    path('split-yes/result/', split_yes_result_view, name='split_yes_result'),
    
    # Results yes calculation page
    path('split-no/', split_no_input, name='no_views'),
    
]
