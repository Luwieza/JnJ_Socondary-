# Import Django shortcuts:
# - render: to display an HTML template
# - redirect: to send the user to another page after success
from django.shortcuts import render, redirect

# Import the SplitNumberForm you created in forms.py
from .form import SplitNumberForm


# Define a view function to handle the split number input page
def split_number_view(request):
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
