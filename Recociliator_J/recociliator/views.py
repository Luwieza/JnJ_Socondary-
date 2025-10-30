# Import Django shortcuts:
# - render: to display an HTML template
# - redirect: to send the user to another page after success
from .calculation_views import split_yes_result
from django.shortcuts import render, redirect # type: ignore
from django.http import HttpResponse

# Import the SplitNumberForm you created in forms.py
from .form import SplitNumberForm


# Main calculator view - entry point for the app
def calculator(request):
    """Main calculator page - redirects to split number input"""
    return redirect('split_number')


# Define a view function to handle the split number input page
def split_number(request):
    # Check if the request is a POST (i.e., the form was submitted)
    if request.method == 'POST':
        # Create a form instance containing the submitted data
        form = SplitNumberForm(request.POST)

        # Validate the form using all the clean methods you defined
        if form.is_valid():
            # Get the cleaned (validated) split number and convert it to an integer
            split_number = int(form.cleaned_data['split_number'])

            # Get the cleaned confirmation string ("yes" or "no")
            confirm_split = form.cleaned_data['confirm_split']

            # Save these values to the user's session so you can use them later
            request.session['split_number'] = split_number
            request.session['confirm_split'] = confirm_split

            # Redirect the user to the next step page
            # Make sure you have a URL named 'next_step' in urls.py
            return redirect('next_step')

    else:
        # If the request is GET (the page is opened normally), create an empty form
        form = SplitNumberForm()

    # Render the template split_input.html, passing the form object to display it
    return render(request, 'split_number.html', {'form': form})


# Next step view - decides which form to show based on user's choice
def next_step(request):
    """Route user to appropriate form based on their yes/no confirmation"""
    # Get the confirmation from session
    confirm_split = request.session.get('confirm_split')

    if not confirm_split:
        # If no session data, redirect back to start
        return redirect('calculator')

    # Route based on user's choice
    if confirm_split == 'yes':
        return redirect('split_yes_input')
    else:  # confirm_split == 'no'
        return redirect('split_no_input')


# Import calculation view function to use it

# Wrapper view for split_yes_result to match URL pattern

def split_yes_result_view(request):
    """Wrapper for the calculation result view"""
    return split_yes_result(request)


def health(request):
    """Lightweight health check endpoint used by load balancers or platforms.

    This intentionally does not touch the database or templates so it is
    safe to call even if other parts of the app fail. Returns plain text OK.
    """
    return HttpResponse("ok", content_type='text/plain')
