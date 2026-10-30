distance = int(input("Enter distance: "))
age = int(input("Enter age: "))

if distance <= 100:
    fare = distance * 2
else:
    fare = distance * 3

if age < 12:
    fare = fare / 2

reservation = 50
total = fare + reservation

print("Ticket Fare:", total)

cancel = input("Cancel ticket? yes/no: ")

if cancel == "yes":
    refund = total * 0.8
    print("Refund Amount:", refund)
else:
    print("Ticket Confirmed")