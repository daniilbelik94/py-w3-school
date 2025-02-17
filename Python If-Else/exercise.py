from operator import index

from main import print_hi

# # 1. Check if a number is positive, negative, or zero
# # Task: Ask the user for a number and check whether it is positive, negative, or zero.
#
#
# print("Task 1: Check if a number is positive, negative, or zero")
# num = int(input("Enter a number: "))
# if num > 0:
#     print(f'{num} is Positive')
# elif num < 0:
#     print(f'{num} is negative')
# else:
#     print(f'{num} is Zero!')







# # 2. Check if a number is even or odd
# # Task: Ask the user for a number and determine whether it is even or odd.
# print("Task 2: Check if a number is even or odd")
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f'The {num} is even')
# else:
#     print(f'The {num} is odd')
#
# # # 3. Find the largest of two numbers
# # # Task: Take two numbers as input and print the largest one.
# # print("Task 3: Find the largest of two numbers")
# # num1 = int(input("Enter first number: "))
# # num2 = int(input("Enter second number: "))


#
#
#
# # 4. Find the largest of three numbers
# # Task: Take three numbers as input and print the largest one.

# print("Task 4: Find the largest of three numbers")
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# num3 = int(input("Enter third number: "))
#
# if num1 > num2 and num1 > num3:
#     print(f'{num1} is largest')
# elif num2 > num1 and num2 > num3:
#     print(f'{num2} is largest')
# else:
#     print(f'{num3} is largest')

# # 5. Check if a year is a leap year
# # Task: Ask the user for a year and check if it is a leap year (divisible by 4 but not 100, except when also divisible by 400).
#
#
# print("Task 5: Check if a year is a leap year")
# year = int(input("Enter a year: "))
#
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f'{year} is a leap year')
# else:
#     print(f'{year} is not leap year')



#
# # 6. Check if a character is a vowel or consonant
# # Task: Ask the user for a letter and determine whether it is a vowel or a consonant.

# print("Task 6: Check if a character is a vowel or consonant")
# char = input("Enter a letter: ").lower()
#
#
# if char in 'aeiou':
#     print(f'{char} is a vowel') # Vowel
# elif char.isalpha() and len(char) == 1:
#     print(f'{char} is a consonant')  # Consonant
# else:
#     print("Please enter a valid letter")

# # 7. Check if a number is within a range (1-100)
# # Task: Ask the user for a number and check if it falls within the range 1 to 100.
#
#
# print("Task 7: Check if a number is within range (1-100)")
# num = int(input("Enter a number: "))
#
# if num in range(1,101):
#     print(f'{num} is in a range of 1 to 100')
# else:
#     print(f'{num} is not in a range of 1 to 100')


# # 8. Check if a password is correct
# # Task: Ask the user for a password and check if it matches a predefined correct password.
#
#
# print("Task 8: Check if a password is correct")
# password = input("Enter the password: ")
# correct_password = "secure123"
#
# if password != correct_password:
#     print(f'{password} is not correct!')
# else:
#     print(f'{password} is correct!')



# # 9. Check if a number is divisible by both 3 and 5
# # Task: Ask the user for a number and check if it is divisible by both 3 and 5.
#
#
# print("Task 9: Check if a number is divisible by both 3 and 5")
# num = int(input("Enter a number: "))
#
# if num % 3 == 0 and num % 5 == 0:
#     print(f'{num} is divisible by both 3 and 5')
# else:
#     print(f'{num} is not divisible by both 3 and 5')



# # 10. Grading system (A, B, C, D, F)
# # Task: Ask the user for a test score (0-100) and assign a letter grade based on the score:
# #
# # 90-100: A
# # 80-89: B
# # 70-79: C
# # 60-69: D
# # Below 60: F
#
# print("Task 10: Grading system")
# score = int(input("Enter your test score: "))
# if score >= 90:
#     print(f'{score} is A')
# elif score >= 80:
#     print(f'{score} is B')
# elif score >= 70:
#     print(f'{score} is C')
# elif score >= 60:
#     print(f'{score} is D')
# else:
#     print(' you are idiot')

