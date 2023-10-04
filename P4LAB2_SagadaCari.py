#Name
#Date 10/4/23
#This is an intro to loops using the range ()

int_1 = int(input("Enter a num: "))
int_2 = int(input("Enter a num: "))

#If first number is smaller
if int_1 <= int_2:
    #Execute for loop using range(start, stop, increment)
    for X in range(int_1, int_2+1, 5):
        print(X)

else:
    print("The first number must be smaller. ")
