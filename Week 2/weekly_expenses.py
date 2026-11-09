# This program calculates a student's weekly expenses.
name = input("Student name;")
daily_transport = float(input("Daily transport cost: "))
daily_feeding = float(input("Daily feeding cost: "))
days = int(input("Days on campus: "))
other = float(input("Other weekly expenses: "))

transport_total = daily_transport * days
feeding_total = daily_feeding * days
weekly_total = transport_total + feeding_total + other

print("WEEKLY EXPENSE SUMMARY")
print("Student:", name)
print(f"Transport total:NGN {transport_total:,.2f}")
print(f"Feeding total: NGN {feeding_total:,.2f}")
print(f"Other expenses: NGN {other:,.2f}")
print(f"Weekly total: NGN {weekly_total:,.2f}")





















