# This is to print the title
print(" Welcome to tip calculator")
bill = float(input("Enter the total bill: $"))
tip = int(input("How many percent? 10, 12, 15 "))
people = int(input ("How many People to split the bill? "))

#Calculate tip percentage
tip_percent = tip / 100

#Total tip amount
total_tip_amount = bill * tip_percent

#Total Bill
total_bill = bill + total_tip_amount
#sSplit the bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Your total bill is {final_amount}")








