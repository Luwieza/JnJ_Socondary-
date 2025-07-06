from django.shortcuts import render, redirect
from .form import SplitYesForm

# 🎯 Displays the form for the user to input all the data
def split_yes_input(request):
    if request.method == 'POST':
        # Form submitted
        form = SplitYesForm(request.POST)
        if form.is_valid():
            # Save the cleaned data to the session
            request.session['split_yes_data'] = form.cleaned_data
            # Redirect to the calculation result page
            return redirect('split_yes_result')
    else:
        # If GET request, instantiate an empty form
        form = SplitYesForm()
    
    # Render the form template
    return render(request, 'split_yes_input.html', {'form': form})
