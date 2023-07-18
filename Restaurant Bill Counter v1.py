# Add Restaurant Bill Counter Heading
print("Restaurant Bill Counter")
print ("_ _ _ _ _ _ _ _ _ _ _ _ ")
#add cost of of meal
cost_of_meal = input("How much did your meal cost? ")
#tax impose insert code
tax_imposed  = float(cost_of_meal) / float(100) * float(16)
#tip???
given_tip = input("Tip kitni do ge? ")
tip_calculation = float(cost_of_meal) / float(100) * float(given_tip)
# TOTAL BILL INSERT
total_bill = float(cost_of_meal) + float(tax_imposed) + float(tip_calculation)
print(total_bill)
if total_bill < 200:
    print("dallay broke mf")
else:
    print("Have a nice evening")