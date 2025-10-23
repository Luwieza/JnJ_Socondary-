from django import forms

# 🎯 This form handles all fields for confirm_split == 'yes'
class SplitYesForm(forms.Form):
    # 1️⃣ First carton number must be '001' or '002'
    first_carton_num = forms.CharField(
        label="First Carton Number",
        widget=forms.TextInput(attrs={'placeholder': '001 or 002'}),
        max_length=3
    )

    # 2️⃣ Lenses to pack (3000–27000)
    lenses_to_pack = forms.IntegerField(
        label="Lenses to Pack",
        min_value=3000,
        max_value=27000,
        help_text="Hint: Use HMI data to view and calculate total lenses to be packed."
    )

    # 3️⃣ Number of lenses in one case (only 1440 or 30000 allowed)
    num_of_lenses_per_case = forms.IntegerField(
        label="Number of Lenses in One Case",
    )

    # 4️⃣ QC samples (60–800)
    qc_sample = forms.IntegerField(
        label="Quantity of Samples",
        min_value=60,
        max_value=800
    )

    # 5️⃣ Cases packed (2–20)
    case_packed = forms.IntegerField(
        label="Cases/Boxes Packed",
        min_value=2,
        max_value=20
    )

    # 6️⃣ Lenses per carton (only 30 or 90 allowed)
    lenses_per_carton = forms.IntegerField(
        label="Lenses per Carton",
    )

    # 7️⃣ Total cartons in partial case (1–100)
    total_cartons_p = forms.IntegerField(
        label="Total Cartons in Partial Case",
        min_value=1,
        max_value=100
    )

    # --- Custom Cleaners for restricted choices ---

    def clean_first_carton_num(self):
        data = self.cleaned_data['first_carton_num'].strip()
        # Must be 001 or 002
        if data not in ('001', '002'):
            raise forms.ValidationError(
                "Invalid input, Please enter between 001 and 002, or else consult your line leader."
            )
        # Return as int for consistency with calculation logic
        return int(data)

    def clean_num_of_lenses_per_case(self):
        data = self.cleaned_data['num_of_lenses_per_case']
        if data not in (1440, 3000):
            raise forms.ValidationError(
                "Invalid input. Please enter either 1440 or 3000."
            )
        return data

    def clean_lenses_per_carton(self):
        data = self.cleaned_data['lenses_per_carton']
        if data not in (30, 90):
            raise forms.ValidationError(
                "Invalid input. Please enter either 30 or 90."
            )
        return data
