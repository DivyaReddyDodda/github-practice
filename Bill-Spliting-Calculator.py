Total_bill = float(input("Enter the total bill amount: "))
Number_of_people = int(input("Enter the number of people to split the bill: "))
Bill_per_person = Total_bill / Number_of_people
print("Each person should pay: $", round(Bill_per_person, 2))