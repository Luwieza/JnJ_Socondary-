# -----------------------------------------------
# Import Django utilities
from django.shortcuts import render, redirect

# Import your SplitNoForm
from .form_no import SplitNoForm
# -----------------------------------------------

def split_no_view(request):
    """
    View to process the workflow when the user confirms 'No' (not the last split).
    """

    if request.method == 'POST':
        # Bind the form with submitted POST data
        form = SplitNoForm(request.POST)

        if form.is_valid():
            # Retrieve cleaned data
            first_carton_num = int(form.cleaned_data['first_carton_num'])
            num_of_lenses_per_case = form.cleaned_data['num_of_lenses_per_case']
            qc_sample = form.cleaned_data['qc_sample']
            case_packed = form.cleaned_data['case_packed']
            lenses_per_carton = form.cleaned_data['lenses_per_carton']
            total_cartons_p = form.cleaned_data['total_cartons_p']

            # Hard-code lenses_to_pack
            lenses_to_pack = 28000

            # Calculate packed products (excluding partial case)
            quantity_of_packed_products = case_packed * num_of_lenses_per_case

            # Calculate partial case
            partial_case = lenses_per_carton * total_cartons_p

            # Calculate total packed including partial case + sample
            total_quantity_of_packed_products = (
                quantity_of_packed_products + partial_case + qc_sample
            )

            # Check if over packed
            if total_quantity_of_packed_products >= lenses_to_pack:
                difference = total_quantity_of_packed_products - lenses_to_pack
                # Render error template (or same page with error)
                return render(
                    request,
                    'split_no_result.html',
                    {
                        'error_message': (
                            f"❌ Error: You have packed {difference} lenses MORE than the total lenses to pack. "
                            "Please check your inputs and try again."
                        )
                    },
                )

            # Calculate rejected products
            quantity_of_rejected_products = lenses_to_pack - total_quantity_of_packed_products

            # Validation: sum must match
            sum_of_all_lenses = (
                total_quantity_of_packed_products + quantity_of_rejected_products
            )

            if sum_of_all_lenses == lenses_to_pack:
                # Everything is valid, display results
                return render(
                    request,
                    'split_no_result.html',
                    {
                        'split_number': request.session.get('split_number'),
                        'first_carton_num': first_carton_num,
                        'qc_sample': qc_sample,
                        'quantity_of_rejected_products': quantity_of_rejected_products,
                        'success': True,
                    },
                )
            else:
                difference = abs(sum_of_all_lenses - lenses_to_pack)
                return render(
                    request,
                    'split_no_result.html',
                    {
                        'error_message': (
                            f"❌ Validation failed by {difference} lenses. Please recheck your inputs."
                        )
                    },
                )

    else:
        # For GET request, show an empty form
        form = SplitNoForm()

    return render(request, 'no.html', {'form': form})
