period_for_calculations = int(input())
doctors = 7
treated_patients = 0
not_treated_patients = 0
for period in range(1, period_for_calculations + 1):
    number_of_patients = int(input())
    if period % 3 == 0:
        if not_treated_patients > doctors:
            doctors += 1
    if doctors >= number_of_patients:
        treated_patients += number_of_patients
    else:
        treated_patients += doctors
        not_treated_patients += number_of_patients - doctors
print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {not_treated_patients}.")
