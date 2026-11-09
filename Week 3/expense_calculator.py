# Student Weekly Expense Calculator - Week 3

# Collect student information
name = input("Student name: ")

# Collect and validate daily transport expense
daily_transport = float(input("Daily transport cost: NGN "))
while daily_transport < 0:
    print("Error! Expense cannot be negative.")
    daily_transport = float(input("Enter daily transport cost again: NGN "))

# Collect and validate daily feeding expense
daily_feeding = float(input("Daily feeding cost: NGN "))
while daily_feeding < 0:
    print("Error! Expense cannot be negative.")
    daily_feeding = float(input("Enter daily feeding cost again: NGN "))

# Collect and validate number of days
days = int(input("Days on campus: "))
while days < 0:
    print("Error! Number of days cannot be negative.")
    days = int(input("Enter days on campus again: "))

# Collect and validate other weekly expenses
other = float(input("Other weekly expenses: NGN "))
while other < 0:
    print("Error! Expense cannot be negative.")
    other = float(input("Enter other weekly expenses again: NGN "))

# Calculate weekly expenses
transport_total = daily_transport * days
feeding_total = daily_feeding * days
weekly_total = transport_total + feeding_total + other

# Display weekly expense summary
print("\nWEEKLY EXPENSE SUMMARY")
print("Student:", name)
print(f"Transport total: NGN {transport_total:,.2f}")
print(f"Feeding total: NGN {feeding_total:,.2f}")
print(f"Other expenses: NGN {other:,.2f}")
print(f"Weekly total: NGN {weekly_total:,.2f}")

# Collect and validate weekly budget
budget = float(input("\nEnter your weekly budget: NGN "))
while budget < 0:
    print("Error! Budget cannot be negative.")
    budget = float(input("Enter your weekly budget again: NGN "))

# Compare expenses with budget
print("\nBUDGET SUMMARY")

if weekly_total < budget:
    remaining = budget - weekly_total
    print("Status: WITHIN BUDGET")
    print(f"Amount remaining: NGN {remaining:,.2f}")

elif weekly_total == budget:
    print("Status: EXACTLY ON BUDGET")
    print("Amount remaining: NGN 0.00")

else:
    exceeded = weekly_total - budget
    print("Status: OVER BUDGET")
    print(f"Amount exceeded: NGN {exceeded:,.2f}")
