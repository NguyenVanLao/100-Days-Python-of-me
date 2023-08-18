#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# Enter total bill
print("Welcome to the tip calculator")
total_bill = input("What was the total bill: $")
# Select tip
per_tip = input(
    "What percentage tip would you like to give (10, 12, or 15% ?):  ")
# Many people to pay
people_pay = input("How many people to split the bill: ")

# Convert data types
total_bill = float(total_bill)
per_tip = int(per_tip)
people_pay = int(people_pay)
# calculate the invoice
each_people_pay = (total_bill / people_pay) * (1 + (per_tip / 100))
# Round result
each_people_pay = round(each_people_pay, 2)
each_people_pay = "{:.2f}".format(each_people_pay) # get to 2 decimal places (33.60)

# print how much money do person to pay
print("Each person should pay: ", each_people_pay)
