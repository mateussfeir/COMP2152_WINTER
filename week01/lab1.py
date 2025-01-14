# Sample Coding Questions 01 Week 01
# Mateus de Souza Carvalho Melco Sfeir
array = [1, 4, 7, 9]
a=1
b=2
c=3
d=4
# The fully bracketed version of
# e = a * c - b / d is
# e = (a * c) - (b / d)
# Given the following line of code, give the Fully-Bracketed Version of:
# e = a - b ** c // d + a % c
E = (a - (b ** c)) // d + a % c

temperature = 32.6
print("The temperature today is " + str(temperature) + " degrees Celsius.")

# Common Functions: Ask the user to input their age, and then save that input into the variable
# “userAge”. For the user input, add 22.Then print the following sentence followed by the value
# of userAge. “Now showing the shop items filtered by age: 22”. Do not hard code the number 22.

userAge = int(input("Enter your age:"))
userAge += 22
print ("Now showing the shop items filtered by age: " + str(userAge))