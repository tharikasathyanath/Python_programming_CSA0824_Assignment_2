# Q1 - Electricity Subsidy Eligibility

households = [
    (1, 100, False, False),
    (2, 101, True, False),
    (3, 150, False, False),
    (4, 200, True, False),
    (5, 201, False, True),
    (6, 250, False, False),
    (7, 80, False, False),
    (8, 180, True, True)
]

print("Using Separate If Statements")

for number, units, ration, senior in households:
    print("\nHousehold:", number)
    if units <= 100:
        print("Full Subsidy")

    if 101 <= units <= 200 and ration:
        print("Partial Subsidy")

    if units > 200 and senior:
        print("Special Subsidy")

    if units > 200 and not senior:
        print("No Subsidy")

    if 101 <= units <= 200 and not ration:
        print("No Subsidy")


print("\nUsing If-Elif-Else Statements")

for number, units, ration, senior in households:
    print("\nHousehold:", number)

    if units <= 100:
        print("Full Subsidy")

    elif 101 <= units <= 200 and ration:
        print("Partial Subsidy")

    elif units > 200 and senior:
        print("Special Subsidy")

    else:
        print("No Subsidy")