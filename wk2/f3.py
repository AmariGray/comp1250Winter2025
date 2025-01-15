# gas calculation program
# ask the user for the current gas price per liter
# ask the user how much money they can afford spending
# tell the user how many litres of gas they can put in their car

print("Welcome to our Gas Calculation Program")
print("You will enter the gas price")
print("You will enter your pre-paid gas amount")
print("We will tell you how many litres of gas you will receive")

gas_price = float(input("Enter the gas price: "))
pre_paid_amount = int(input("Enter your prepaid amount: "))
print(pre_paid_amount, "dollars worth of gas at a rate of",
      gas_price, "will give you",
      pre_paid_amount/gas_price, "litres of gas")
