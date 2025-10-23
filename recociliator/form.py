# Import Django's form tools
from django import forms

# -------------------------- CLASS OF FORM FIELDS ---------------------------------------

# Defines a Class that consist of form fields.
class SplitNumberForm(forms.Form):
    
    # Form field of split_number.
    split_number = forms.CharField(
        label="Enter a split number", # Label shown above or beside the field
        max_length=3,                 # Maximum of 3 characters allowed
        
        # Greyed-out dictionary  hint text in the input box
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 001'}),
    )

    # Form field to confirm  split.
    confirm_split = forms.CharField(
        # Label shown above or beside the field
        label="Are you working on the last split? Confirm 'Yes' or 'No'",
        max_length=3, # Maximum of 3 characters allowed.
        widget=forms.TextInput(attrs={'placeholder': 'Yes or No'}), 
    )
    
# ---------------------------- CUSTOM VALIDATION ---------------------------------------

    # Custom validation function/method for split_number.
    def clean_split_number(self): # Use a django method for verification clean_fieldName.
      
        # Retrieve the raw input value, remove any extra spaces.
        data = self.cleaned_data['split_number'].strip()
        
        # Create a list of valid split numbers as zero-padded strings ('001' to '014')
        valid_numbers = [str(x).zfill(3) for x in range(1, 15)]
        
         # Check if the entered split number is valid
        if data not in valid_numbers:
            # If not valid, raise an error that will be displayed to the user.
            raise forms.ValidationError(  
                "Invalid input: please enter a numeric value, from 001 to 014."
            )
        # Return the cleaned and validated data.
        return data

    # Validation function for confirm_split.
    def clean_confirm_split(self): # Use a django method for verification clean_fieldName.
      
        # Retrieve the raw input, remove spaces, convert to lowercase
        data = self.cleaned_data['confirm_split'].strip().lower()
        if data not in ('yes', 'no'): # Check if the input is either 'yes' or 'no'
          
            # If not valid, raise an error that will be displayed to the user.
            raise forms.ValidationError(
                "Invalid input. Please enter Yes or No."
            )
        # Return the cleaned and validated data.
        return data

