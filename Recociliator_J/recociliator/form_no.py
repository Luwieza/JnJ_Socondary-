# -------------------- IMPORT DJANGO FORM CLASSES --------------------
from django import forms


# -------------------- FORM FOR confirm_split == 'no' --------------------
class SplitNoForm(forms.Form):
    """
    A dedicated form to collect all inputs
    when the user confirms 'No' (not the last split).
    """

    # First carton number: must be '001' or '002'
    first_carton_num = forms.CharField(
        label="Enter the first carton number",
        max_length=3,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., 001'}),
    )

    # Number of lenses in a case/box: 1440 or 30000
    num_of_lenses_per_case = forms.IntegerField(
        label="Enter the total number of lenses in a case/box",
        widget=forms.NumberInput(attrs={'placeholder': '1440 or 30000'}),
    )

    # Quantity of samples: 60–800
    qc_sample = forms.IntegerField(
        label="Enter quantity of samples",
        widget=forms.NumberInput(attrs={'placeholder': 'Between 60 and 800'}),
    )

    # Number of fully packed cases: 2–20
    case_packed = forms.IntegerField(
        label="Enter total packed cases (excluding partial case)",
        widget=forms.NumberInput(attrs={'placeholder': '2 to 20'}),
    )

    # Number of lenses per carton: 30 or 90
    lenses_per_carton = forms.IntegerField(
        label="Enter lenses per carton",
        widget=forms.NumberInput(attrs={'placeholder': '30 or 90'}),
    )

    # Total cartons inside the partial case: 1–100
    total_cartons_p = forms.IntegerField(
        label="Enter total cartons inside partial case",
        widget=forms.NumberInput(attrs={'placeholder': '1 to 100'}),
    )

    # ---------------- VALIDATION METHODS ----------------

    def clean_first_carton_num(self):
        data = self.cleaned_data['first_carton_num'].strip()
        valid_numbers = [str(x).zfill(3) for x in range(1, 3)]  # '001', '002'
        if data not in valid_numbers:
            raise forms.ValidationError(
                "Invalid input: please enter 001 or 002."
            )
        return data

    def clean_num_of_lenses_per_case(self):
        data = self.cleaned_data['num_of_lenses_per_case']
        if data not in (1440, 30000):
            raise forms.ValidationError(
                "Invalid input: please enter 1440 or 30000."
            )
        return data

    def clean_qc_sample(self):
        data = self.cleaned_data['qc_sample']
        if not (60 <= data <= 800):
            raise forms.ValidationError(
                "Invalid input: please enter a value between 60 and 800."
            )
        return data

    def clean_case_packed(self):
        data = self.cleaned_data['case_packed']
        if not (2 <= data <= 20):
            raise forms.ValidationError(
                "Invalid input: please enter a value between 2 and 20."
            )
        return data

    def clean_lenses_per_carton(self):
        data = self.cleaned_data['lenses_per_carton']
        if data not in (30, 90):
            raise forms.ValidationError(
                "Invalid input: please enter 30 or 90."
            )
        return data

    def clean_total_cartons_p(self):
        data = self.cleaned_data['total_cartons_p']
        if not (1 <= data <= 100):
            raise forms.ValidationError(
                "Invalid input: please enter a value between 1 and 100."
            )
        return data
