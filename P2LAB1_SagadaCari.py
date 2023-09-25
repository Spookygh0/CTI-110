# FirstName LastName
# 9/25/2023
# Calcuate cost of driving



#Get input from user as float
mpg = float(input("How many mpg does the car get?"))
gas_price = float(input("Hoe much does one gallon of gas cost?"))
#Calculate cost
twenty_miles = (20/mpg)*gas_price
seventyfive_miles = (75/mpg)*gas_price
fivehundred_miles = (500/mpg)*gas_price
#Display to user
print(f'The cost to drive 20 miles: {twenty_miles:.2f}')
