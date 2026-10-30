hotel = float(input("Enter hotel expense: "))
food = float(input("Enter food expense: "))
travel = float(input("Enter travel expense: "))

rate = float(input("Enter exchange rate: "))
fee = float(input("Enter conversion fee percentage: "))
budget = float(input("Enter budget in rupees: "))

total = (hotel + food + travel) * rate
conversion_fee = total * fee / 100
total = total + conversion_fee

print("Total Expense:", total)
print("Conversion Fee:", conversion_fee)

if total <= budget:
    print("Within Budget")
else:
    print("Over Budget")

if hotel >= food and hotel >= travel:
    print("Largest Expense: Hotel")
elif food >= travel:
    print("Largest Expense: Food")
else:
    print("Largest Expense: Travel")