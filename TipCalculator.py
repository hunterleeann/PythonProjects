total = float(input("Please enter the meal total: $"))
tip = float(input("How much do you want to tip? 10, 12, or 15 percent? "))
split = float(input("How many people need to split the bill? "))

total = (total / split) * ((tip/100) + 1)

total = round(total, 2)

print(f"Each person owes: ${total} ")