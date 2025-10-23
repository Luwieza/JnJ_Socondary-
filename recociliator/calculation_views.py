from django.shortcuts import render
from django.http import HttpResponse

# 🎯 Performs calculations and shows results or errors


def split_yes_result(request):
    # Retrieve stored input from the session
    data = request.session.get('split_yes_data')
    if not data:
        return render(request, 'split_yes_result.html', {
            'success': False,
            'error_message': 'No data found. Please start over.'
        })

    # Extract fields
    first_carton_num = data['first_carton_num']
    lenses_to_pack = data['lenses_to_pack']
    num_of_lenses_per_case = data['num_of_lenses_per_case']
    qc_sample = data['qc_sample']
    case_packed = data['case_packed']
    lenses_per_carton = data['lenses_per_carton']
    total_cartons_p = data['total_cartons_p']

    # Calculate quantities
    quantity_of_packed_products = case_packed * num_of_lenses_per_case
    partial_case = lenses_per_carton * total_cartons_p
    total_quantity_of_packed_products = (
        quantity_of_packed_products + partial_case + qc_sample
    )

    # Check for over packing
    if total_quantity_of_packed_products >= lenses_to_pack:
        difference = total_quantity_of_packed_products - lenses_to_pack
        return render(request, 'split_yes_result.html', {
            'success': False,
            'error_message': f"❌ Error: You have packed {difference} lenses MORE than the total lenses to pack. Please check your inputs and try again."
        })

    # Calculate rejected lenses
    quantity_of_rejected_products = lenses_to_pack - total_quantity_of_packed_products
    sum_of_all_lenses = total_quantity_of_packed_products + quantity_of_rejected_products

    # Final validation
    if sum_of_all_lenses != lenses_to_pack:
        difference = abs(sum_of_all_lenses - lenses_to_pack)
        return render(request, 'split_yes_result.html', {
            'success': False,
            'error_message': f"❌ Validation failed by {difference} lenses. Please recheck your inputs."
        })

    # Get split number from session for display
    split_number = request.session.get('split_number', 'N/A')

    # Success output
    return render(request, 'split_yes_result.html', {
        'success': True,
        'split_number': split_number,
        'first_carton_num': first_carton_num,
        'qc_sample': qc_sample,
        'quantity_of_rejected_products': quantity_of_rejected_products
    })
