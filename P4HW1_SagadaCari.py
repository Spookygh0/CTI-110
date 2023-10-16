#FirstName LastName
#Date


#This is a function
def num_to_letter(number):

  if number <= 100 and number >=90:
    letter = "A"

  elif number <= 89 and number >=80:
    letter = "B"

  elif number <= 79 and number >=70:
    letter = "C"

  elif number <=69 and number >=60:
    letter = "D"

  else:
    letter = "F"

  return letter


#Ask user - how many gardes will you enter?
num_grades = int(input("How many grades will you enter? "))

#Create an empty list
grades_list = []

for value in range(num_grades):
    grade = int(input(f"Enter grade #{value+1}: "))
    if grade >= 0 and grade <= 100:
        grades_list.append(grade)
    else:
        while grade < 0 or grade > 100:
            print("INVALID GRADE ENTERED! ")
            print("Grade should be between 0 and 100 ")
            grade = int(input(f"Re-enter grade #{value+1}: "))
        grades_list.append(grade)

#Drop the lowest grade from the list
min_grade = min(grades_list)

#The remove() method does not return to a value, what does that mean?
grades_list.remove(min_grade)

#Get the average (mean) value of the list
average = (sum(grades_list))/len(grades_list)

#Display results
print("-----------Results----------")
print(f"The lowest grade is: {min_grade}")
print(f"Grades after dropping lowest: {grades_list}")
print(f"Average: {average}")
print(f"Letter Grade: {num_to_letter(average)}")
