# FirstName LastName
#9/25/23
#Displays  floating-point notation


num1 = float(input("Enter a float number:"))
num2 = float(input("Enter a float number:"))
num3 = float(input("Enter a float number:"))
num4 = float(input("Enter a float number:"))

product = num1*num2*num3*num4
average = (num1+num2+num3+num4)/4

print(f'{product:.0f}\t{average:.0f}')
print(f'{product:.3f}\t{average:.3f}')

