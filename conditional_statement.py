# # if-else condition statement
# var1 = 18
# age = int(input("How old are you? "))

# if age >= var1:
#     print("You are an adult")
# else:
#     print("You are a child")

# if else-if else condition statement
grade = input("What was your grade: ")

if grade.lower() == "a":
    print(f'Your grade is {5.0}')
elif grade.lower() == "b":
    print(f'Your grade is {4.0}')
elif grade.lower()=="c":
    print(f'Your grade is {3.0}')
elif grade.lower()=="d":
    print(f'Your grade is {2.0}')
elif grade.lower() == "f":
    print(f'Your grade is {0.0}')
else:
    print("You failed")