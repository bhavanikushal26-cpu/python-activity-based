n = int(input("Enter number of products: "))

total = 0

for i in range(n):
    price = float(input("Enter product price: "))
    qty = int(input("Enter quantity: "))

    amount = price * qty
    total = total + amount

if total >= 1000:
    discount = total * 0.10
else:
    discount = 0

if discount > 200:
    discount = 200

amount = total - discount
tax = amount * 0.05
bill = amount + tax

print("Total Amount:", total)
print("Discount:", discount)
print("Tax:", tax)
print("Final Bill:", bill)