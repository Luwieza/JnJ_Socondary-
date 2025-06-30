import math
"""
  A tool used to calculate the tal number of rejected Arrays
  (lenses) per split.
  
  List of things to fix.
  
  1 Conduct tests, using the following:
                
                a Decimals
                b Strings
                c Alphabets
                d Minimum strings in range numbers
                e Maximum strings in range numbers
                f Medium  strings in range numbers
                g Leading zeros be strings
                h Use a real problem.
                
  2 Structure prompt messages short and correctly
  3 Well structure to prove prompt message
  4 lastly use django 
  
"""

# Ask user to input split number.
# Generate valid inputs from 001 to 002 using zfill
valid_numbers = [str(x).zfill(3) for x in range(1, 15)]  # ['001', '014']

while True:
  user_input = input("Enter a split number: ").strip() # Remove trail spaces

  # loop through values in valid_numbers.
  if user_input in valid_numbers: 
    # If values entered by user matches with values invalid_numbers,
    # continue to the next step.
    break # Stop the loop if its true.
    
  else: # Continue to loop if its false.
    print("Invalid input: please enter a numeric value, from 001 to 014.")

# Convert the str into int for calculation.
split_number = int(user_input)

# Ask the user to confirm split number, if working on the last split,
# Confirm 'Yes' or 'No'.

valid_words = [
    "yes", "no"
]

while True:
    confirm_split = input("Are you working on the last split? "
                      "Confirm, 'Yes' or 'No': ").strip().lower()
    if confirm_split in valid_words:
        # if input is valid, continue to the next step.
        break
    else:
        print("Invalid input. Please enter Yes or No.")

    # Convert the str into int for calculation.
    confirm_split = (confirm_split)


# --- ===== ------ ===== --- If the user confirms 'yes'--- ===== ------ ===== 
if confirm_split == 'yes':
    while True:

# ASK THE NECESSARY INPUT:
    
    # ======================== FIRST_CARTON_NUMBER ============================
    # Generate valid inputs from 001 to 002 using zfill
        valid_numbers = [str(x).zfill(3) for x in range(1, 3)]  # ['001', '002']
    
        while True:
        
        # Ask user to input numbers.
            first_carton_num = input("Enter the first carton number: ").strip()
        
        #loop through values in valid_numbers.
            if first_carton_num in valid_numbers: # If its true proceed.
                break # valid input, stop the loop and continues.
            else:
                print("Invalid input, Please enter between 001 and "
                    "002, or else consult your line leader.")
    
    # Convert the str into int for calculation.
        first_carton_num = int(first_carton_num) 
    
    
    # ============================ Lense to be packed =======================
    # Generate valid inputs from 3000 to 27000.
        while True:
        
            lenses_to_pack = input("Enter the total quantity of lenses "
                                "to be packed: ").strip()

            if lenses_to_pack.isdigit() and 3000 <= int(lenses_to_pack) <= 27000:
                print("Hint: Use HMI to calculate total lenses to be packed!")
                break  # Stop the loop when its true to the next process.
            else:
                print("Invalid input. Please enter either 3000 or 27000.")
    
    # Convert the str into int for calculation.
        lenses_to_pack = int(lenses_to_pack)
    
    
    # ========================== Number of lenses in one case =================
    # This will only accept two values. (1440, 30000)
        while True:
            num_of_lenses_per_case = input("Enter the total number of lenses "
                                        "in a case/box): ").strip()

            if num_of_lenses_per_case.isdigit() and int(num_of_lenses_per_case) in (1440, 30000):
                break  # valid input
            else:
                print("Invalid input. Please enter either 1440 or 30000.")

    # Convert the str into int for calculation 
        num_of_lenses_per_case = int(num_of_lenses_per_case)


    # ========================= Quantity of sample ===========================
    # Generate valid inputs from from 60 to 800
        while True:
        
        # Ask user to input numbers.
            qc_sample = input("Enter quantity of samples: ").strip()
    
            if qc_sample.isdigit() and 60 <= int(qc_sample) <= 800:
                break # Stop the loop when its true to the next process.
            else:
                print("Invalid input. Please enter values between 60 and 800.")

    # Convert the str into int for calculation 
        qc_sample = int(qc_sample)
    
    
    # =========================== Cases/boxes packed ==========================
    # Generate valid inputs from from 02 to 20
        while True:
        
        # Ask user to input numbers.
            case_packed = input("Enter the total number of "
                                "packed case/box (excluding partial case/box): ").strip()
    
            if case_packed.isdigit() and 2 <= int(case_packed) <= 20: 
                break # Stop the loop when its true to the next process.
            else:
                print("Invalid input. Please enter values between 02 and 20.")    
        
    # Convert the str into int for calculation    
        case_packed = int(case_packed)    
    
    
    # ========================== Lenses per carton =============================
    # This will only accept two values (30, 90)
        while True:
        
            lenses_per_carton = input("Enter the total number of lenses in a carton): ").strip()

            if lenses_per_carton.isdigit() and int(lenses_per_carton) in (30, 90):
                break  # while true, stop the loop and proceed to the next process.
            else:
                print("Invalid input. Please enter either 30 or 90.")
            # while false, run the loop from again.
            
    # Convert the str into int for calculation
        lenses_per_carton = int(lenses_per_carton)       
    
    
    # ================ Total number of cartons inside partial case/box ===========
    # Generate valid inputs from 16 to 100
        while True:
        
        # Ask user to input numbers.
            total_cartons_p = input("Enter the total number of "
                                "cartons inside partial case/box: ").strip()
    
            if total_cartons_p.isdigit() and 1 <= int(total_cartons_p) <= 100: 
                break # Stop the loop when its true to the next process.
            else:
                print("Invalid input. Please enter values between 1 and 100.") 
               
    # Convert the str into int for calculation
        total_cartons_p = int(total_cartons_p)

    
    
    # =================== PERFORM CALCULATION ===============================
  
    # Calculate quantity of packed products, excluding partial case/box.
        quantity_of_packed_products = case_packed * num_of_lenses_per_case 
    # Not total quantity, exclude partial case in this stage.  
        
    # Calculate Partial case/box.
        partial_case = lenses_per_carton * total_cartons_p 
    
    
    #                                   PERFORM CHECKS  
    # Calculate the total quantity of packed lenses including partial case/box.
        total_quantity_of_packed_products = quantity_of_packed_products + partial_case + qc_sample

    # Check if total packed + samples exceed lenses to pack:
        if total_quantity_of_packed_products >= lenses_to_pack:
            
            difference = total_quantity_of_packed_products - lenses_to_pack
            print(f"❌ Error: You have packed {difference} lenses MORE than the total lenses to pack.")
            print("Please check your inputs and try again.")
            
            continue # 🔁 Restart loop
   
        
    # Calculate the total rejected lenses correctly:
        quantity_of_rejected_products = lenses_to_pack - total_quantity_of_packed_products
    
    # Validation: sum should always match
        sum_of_all_lenses = total_quantity_of_packed_products + quantity_of_rejected_products

        if sum_of_all_lenses == lenses_to_pack:
            print(f"Split number: {split_number}"
                f"\nCarton number: {first_carton_num}"
                f"\nQC samples: {qc_sample}"
                f"\nRejected lenses: {quantity_of_rejected_products} ✅.")
            
            break # To restart the loop
        
        else:
            difference = abs(sum_of_all_lenses - lenses_to_pack)
            print(f"❌ Validation failed by {difference} lenses. Restarting...")
        # Restart the loop from the beginning
        
        continue # 🔁 Restart loop
    
    
# --- ===== ------ ===== --- If the user confirms 'No'--- ===== ------ ===== ----

if confirm_split == 'no':
    while True:

# ASK THE NECESSARY INPUT:
    
    # ======================== FIRST_CARTON_NUMBER ============================
    # Generate valid inputs from 001 to 002 using zfill
        valid_numbers = [str(x).zfill(3) for x in range(1, 3)]  # ['001', '002']
    
        while True:
        
        # Ask user to input numbers.
            first_carton_num = input("Enter the first carton number: ").strip()
        
        #loop through values in valid_numbers.
            if first_carton_num in valid_numbers: # If its true proceed.
                break # valid input, stop the loop and continues.
            else:
                print("Invalid input, Please enter between 001 and "
                    "002, or else consult your line leader.")
    
    # Convert the str into int for calculation.
        first_carton_num = int(first_carton_num) 
    
    
    # ============================ Lense to be packed =======================
        lenses_to_pack = 28000
    
    
    # ========================== Number of lenses in one case =================
    # This will only accept two values. (1440, 30000)
        while True:
            num_of_lenses_per_case = input("Enter the total number of lenses "
                                        "in a case/box): ").strip()

            if num_of_lenses_per_case.isdigit() and int(num_of_lenses_per_case) in (1440, 30000):
                break  # valid input
            else:
                print("Invalid input. Please enter either 1440 or 30000.")

    # Convert the str into int for calculation 
        num_of_lenses_per_case = int(num_of_lenses_per_case)


    # ========================= Quantity of sample ===========================
    # Generate valid inputs from from 60 to 800
        while True:
        
        # Ask user to input numbers.
            qc_sample = input("Enter quantity of samples: ").strip()
    
            if qc_sample.isdigit() and 60 <= int(qc_sample) <= 800:
                break # Stop the loop when its true to the next process.
            else:
                print("Invalid input. Please enter values between 60 and 800.")

    # Convert the str into int for calculation 
        qc_sample = int(qc_sample)
    
    
    # =========================== Cases/boxes packed ==========================
    # Generate valid inputs from from 02 to 20
        while True:
        
        # Ask user to input numbers.
            case_packed = input("Enter the total number of "
                                "packed case/box (excluding partial case/box): ").strip()
    
            if case_packed.isdigit() and 2 <= int(case_packed) <= 20: 
                break # Stop the loop when its true to the next process.
            else:
                print("Invalid input. Please enter values between 02 and 20.")    
        
    # Convert the str into int for calculation    
        case_packed = int(case_packed)    
    
    
    # ========================== Lenses per carton =============================
    # This will only accept two values (30, 90)
        while True:
        
            lenses_per_carton = input("Enter the total number of lenses in a carton): ").strip()

            if lenses_per_carton.isdigit() and int(lenses_per_carton) in (30, 90):
                break  # while true, stop the loop and proceed to the next process.
            else:
                print("Invalid input. Please enter either 30 or 90.")
            # while false, run the loop from again.
            
    # Convert the str into int for calculation
        lenses_per_carton = int(lenses_per_carton)       
    
    
    # ================ Total number of cartons inside partial case/box ===========
    # Generate valid inputs from 16 to 100
        while True:
        
        # Ask user to input numbers.
            total_cartons_p = input("Enter the total number of "
                                "cartons inside partial case/box: ").strip()
    
            if total_cartons_p.isdigit() and 1 <= int(total_cartons_p) <= 100: 
                break # Stop the loop when its true to the next process.
            else:
                print("Invalid input. Please enter values between 1 and 100.") 
               
    # Convert the str into int for calculation
        total_cartons_p = int(total_cartons_p)

    
    
    # =================== PERFORM CALCULATION ===============================
  
    # Calculate quantity of packed products, excluding partial case/box.
        quantity_of_packed_products = case_packed * num_of_lenses_per_case 
    # Not total quantity, exclude partial case in this stage.  
        
    # Calculate Partial case/box.
        partial_case = lenses_per_carton * total_cartons_p 
    
    
    #                                   PERFORM CHECKS  
    # Calculate the total quantity of packed lenses including partial case/box.
        total_quantity_of_packed_products = quantity_of_packed_products + partial_case + qc_sample

    # Check if total packed + samples exceed lenses to pack:
        if total_quantity_of_packed_products >= lenses_to_pack:
            
            difference = total_quantity_of_packed_products - lenses_to_pack
            print(f"❌ Error: You have packed {difference} lenses MORE than the total lenses to pack.")
            print("Please check your inputs and try again.")
            
            continue # 🔁 Restart loop
   
        
    # Calculate the total rejected lenses correctly:
        quantity_of_rejected_products = lenses_to_pack - total_quantity_of_packed_products
    
    # Validation: sum should always match
        sum_of_all_lenses = total_quantity_of_packed_products + quantity_of_rejected_products

        if sum_of_all_lenses == lenses_to_pack:
            print(f"Split number: {split_number}"
                f"\nCarton number: {first_carton_num}"
                f"\nQC samples: {qc_sample}"
                f"\nRejected lenses: {quantity_of_rejected_products} ✅.")
            
            break # To restart the loop
        
        else:
            difference = abs(sum_of_all_lenses - lenses_to_pack)
            print(f"❌ Validation failed by {difference} lenses. Restarting...")
        # Restart the loop from the beginning
        
        continue # 🔁 Restart loop
