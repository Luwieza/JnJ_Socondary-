# This connects a URL path to the view.
from django.urls import path

from django.urls import path
from .views import calculator, split_number, next_step, split_yes_result_view, health   # views.py
from .yes_views import split_yes_input
from .no_views import split_no_input


urlpatterns = [
    # Home page or default calculator
    path('', calculator, name='home'),

    # Calculator page
    path('calculator/', calculator, name='calculator'),

    # Split number input page
    path('split-number/', split_number, name='split_number'),

    # Next step page
    path('next/', next_step, name='next_step'),

    # Form yes input page
    path('split-yes/', split_yes_input, name='split_yes_input'),

    # Result yes calculation page
    path('split-yes/result/', split_yes_result_view, name='split_yes_result'),

    # Form no input page
    path('split-no/', split_no_input, name='split_no_input'),
    # Simple healthcheck endpoint for load-balancers / deployment platforms
    path('_health/', health, name='health'),

]
