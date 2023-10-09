#Name
#Date 10/9/23
#This program is going to use if statements to gross pay


#Get input from user
name = ""

#Initialise a variable to count the loop iterations
count = 0
total_pay = 0
while name != "Done":
    name = input("Enter employee name: ")
    if name != "Done":
        count = count + 1
        num_hrs = float(input("Enter number of hours worked: "))
        pay_rate = float(input("Enter hourly pay rate: "))
        OT_hrs = 0
        has_OT = False
        OT_pay = 0

        #Calculate overtime - yes/no - how much
        if (num_hrs > 40):
            has_OT = True
            OT_hrs = num_hrs - 40
        else:
            has_OT = False

        if has_OT == True:
            OT_pay = pay_rate*1.5 * (num_hrs - 40) #Actual OT total pay
        else:
            OT_pay = 0
            

        #Calculate regular pay
        reg_pay = pay_rate * (num_hrs - OT_hrs)
        gross_pay = reg_pay + OT_pay
        total_pay = total_pay + gross_pay
        
        #Display name, pay rate, num hrs worked, OT hrs, OT pay, regular pay, gross pay

        print("Name: ", name)
        print("Overtime hours: ", OT_hrs)
        print("Overtime pay: ", OT_pay)
        print("Regular hours: ", num_hrs - OT_hrs)
        print("Regular pay: ", reg_pay + OT_pay)
        
#While loop breaks
print("Total number of employees entered: ", count)
print("Total paid to employees: ", total_pay)

