n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    marks = int(input("Enter aggregate marks: "))
    s1 = int(input("Enter subject 1 marks: "))
    s2 = int(input("Enter subject 2 marks: "))
    attendance = int(input("Enter attendance percentage: "))
    income = int(input("Enter family income: "))

    if marks >= 75 and s1 >= 40 and s2 >= 40 and attendance >= 75 and income <= 200000:
        print(name, "is eligible for scholarship")
    else:
        print(name, "is not eligible for scholarship")
