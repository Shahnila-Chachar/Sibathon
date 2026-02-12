## inputs from user
# total rent
# total food ordered for snacking
# Electricity units consumed
# charge per unit of electricity

## outputs
# total amount to be paid by each person

rent = int(input("Enter your hostel rent: "))
food = int(input("Enter the total amount of food ordered for snacking: "))
electricity_units = int(input("Enter the total electricity units consumed: "))
charge_per_unit = int(input("Enter the charge per unit of electricity: "))
persons_sharing = int(input("Enter the number of people sharing the expenses: "))

total_electricity_charge = electricity_units * charge_per_unit
total_amount = rent + food + total_electricity_charge
amount_per_person = total_amount / persons_sharing
print(f"The total amount to be paid by each person is: {amount_per_person}")
