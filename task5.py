usage = int(input("Enter data usage: "))
days = int(input("Enter validity days: "))
budget = int(input("Enter budget: "))

if usage <= 2 and days <= 28 and budget >= 199:
    print("Plan 1 is best")
    print("Cost = 199")

elif usage <= 3 and days <= 28 and budget >= 299:
    print("Plan 2 is best")
    print("Cost = 299")

elif usage <= 2 and days <= 56 and budget >= 399:
    print("Plan 3 is best")
    print("Cost = 399")

else:
    print("No suitable plan")7, 55