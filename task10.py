venue = int(input("Enter venue cost: "))
equipment = int(input("Enter equipment cost: "))
catering = int(input("Enter catering cost: "))
transport = int(input("Enter transport cost: "))
certificate = int(input("Enter certificate cost per person: "))

sponsor = int(input("Enter sponsorship amount: "))
fee = int(input("Enter registration fee per person: "))

cost = venue + equipment + catering + transport

remaining = cost - sponsor

if remaining < 0:
    remaining = 0

people = remaining // fee

if remaining % fee != 0:
    people = people + 1

total = cost + certificate * people
contribution = total - sponsor

print("Total Fixed Cost:", cost)
print("Sponsorship Shortfall:", remaining)
print("Minimum Participants:", people)
print("Total Cost:", total)
print("Participant Contribution:", contribution)