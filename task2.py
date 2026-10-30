n = int(input("Enter number of months: "))
units_list = []
bills = []

for i in range(n):
    units = int(input("Enter electricity units: "))

    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    bill = bill + 50

    if bill > 1000:
        bill = bill + 100
    else:
        bill = bill - 20

    units_list.append(units)
    bills.append(bill)

print("\nMonthly Electricity Bills")

for i in range(n):
    print("Month", i + 1, "Units:", units_list[i], "Bill:", bills[i])

    if i > 0 and bills[i] > bills[i - 1] * 1.5:
        print("Unusual increase in bill")
