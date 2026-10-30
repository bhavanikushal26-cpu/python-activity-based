name = input("Enter patient name: ")

c = int(input("Enter consultation charges: "))
d = int(input("Enter diagnostic charges: "))
t = int(input("Enter treatment charges: "))

total = c + d + t

if c < 0 or d < 0 or t < 0:
    print("Invalid charges")
else:
    if total >= 5000:
        discount = total * 10 / 100
    else:
        discount = 0

    bill = total - discount

    if bill >= 5000:
        print("High Payment")
    elif bill >= 2000:
        print("Medium Payment")
    else:
        print("Low Payment")

    print("Patient Name:", name)
    print("Total Bill:", total)
    print("Discount:", discount)
    print("Final Bill:", bill)
