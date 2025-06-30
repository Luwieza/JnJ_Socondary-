from django.shortcuts import render
from django.http import HttpResponse
import math

def calculator(request):
    result = None
    error_message = None

    if request.method == "POST":
        try:
            split_number = request.POST.get("split_number")
            is_last_split = request.POST.get("is_last_split", "").strip().lower()
            lenses_to_pack = int(request.POST.get("lenses_to_pack"))
            case_packed = int(request.POST.get("case_packed"))
            qc_sample = int(request.POST.get("qc_sample"))
            lenses_per_carton = int(request.POST.get("lenses_per_carton"))
            total_cartons_p = int(request.POST.get("total_cartons_p"))

            # Logic begins - following your console script exactly
            if lenses_to_pack not in [1440, 30000]:
                error_message = "Lenses to pack must be either 1440 or 30000."
            elif is_last_split not in ["yes", "no"]:
                error_message = "Are you working on the last split? Confirm, 'Yes' or 'No'."
            else:
                total_lenses_in_cases = case_packed * lenses_per_carton
                total_partial = total_cartons_p * lenses_per_carton
                sum_of_all_lenses = total_lenses_in_cases + total_partial + qc_sample
                total_rejects = lenses_to_pack - sum_of_all_lenses

                result = {
                    "split_number": split_number,
                    "total_rejects": total_rejects,
                    "check_answer": f"{lenses_to_pack} - ({total_lenses_in_cases} + {total_partial} + {qc_sample}) = {total_rejects}"
                }

        except ValueError:
            error_message = "Please enter valid numeric values in all required fields."

    return render(request, "index.html", {"result": result, "error": error_message})
