

# 1. Count even and odd numbers in a list
# Task: Given a list of numbers, count how many are even and how many are odd.




print("Task 1: Count even and odd numbers in a list")

numbers = [12, 7, 5, 64, 14, 23, 90, 11, 6, 8]


# Your code here
def counter(numbers):
    even_count = 0
    odd_count = 0
    for i in numbers:
        if i % 2 == 0:
            even_count +=1
        elif i % 2 != 0:
            odd_count +=1
    return even_count, odd_count

even_count, odd_count = counter(numbers)



print(f"Even numbers count: {even_count}")
print(f"Odd numbers count: {odd_count}")


# 2. Filter adults from a dictionary
# Task: Given a dictionary with names and ages, create a new dictionary with only adults (age 18 and above).


print("Task 2: Filter adults from a dictionary")

people = {
    "Alice": 25,
    "Bob": 17,
    "Charlie": 19,
    "David": 16
}

adults = {}

# Your code here

def filter_adults(people):
    adults = {}
    for x,y in people.items():
        if y >= 18:
            adults[x] = y
    return adults

adults = filter_adults(people)


print("Adults:", adults)


# 3. Merge and sort two sets
# Task: Combine two sets and return a sorted list of unique elements.


print("Task 3: Merge and sort two sets")

set1 = {3, 6, 8, 1, 2}
set2 = {5, 2, 9, 6, 4}

# Your code here

def combined_sets(set1,set2):
    sorted_set = sorted(set1 | set2)
    return list(sorted_set)



sorted_set = combined_sets(set1,set2)
print("Merged and sorted set:", sorted_set)


# 4. Update values in a dictionary
# Task: Increase the prices of all products in the dictionary by 10%.

print("Task 4: Update values in a dictionary")

products = {
    "Bread": 50,
    "Milk": 90,
    "Meat": 250,
    "Cheese": 120,
    "Yogurt": 80
}

# Your code here
def upd_values(products):
    for x,y in products.items():
        products[x] = round(y * 1.10)
    return products

new_values = upd_values(products)
print("Updated prices:", new_values)
#
#
# 5. Convert a list to a tuple and print elements
# Task: Convert a given list into a tuple and print each element of the tuple.

print("Task 5: Convert a list to a tuple and print elements")

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers_tuple = tuple(numbers_list)


# Your code here



print("Tuple from list:", numbers_tuple)
print("Tuple elements:")
for num in numbers_tuple:
    print(num)


# 6. Reverse a string using a loop
# Task: Reverse a given string using a loop.


print("Task 6: Reverse a string using a loop")

text = "Python"
reversed_text = ""
# Your code here

def revers(text):
    reversed_text = ""
    for x in text:
        reversed_text = x + reversed_text
    letter_count = sum(1 for x in text if x.isalpha())
    return reversed_text, letter_count


reversed_text, letter_count = revers(text)
print("Original text:", text)
print("Reversed text:", reversed_text)


# # 7. Count vowels in a word
# # Task: Count the number of vowels in the given word.
#
#
#
print("Task 7: Count vowels in a word")

word = "education"
vowel_count = 0

# Your code here

def count_vowels(text):
    vowel = 'aeiou'
    vowel_count = 0
    for x in text:
        if x.lower() in vowel:
            vowel_count += 1
    return vowel_count

vowel_count = count_vowels(word)


print(f"Number of vowels in '{word}': {vowel_count}")
#
#
# 8. Find duplicates in a list
# Task: Identify and store duplicate numbers from a given list.


print("Task 8: Find duplicates in a list")

numbers = [4, 5, 9, 4, 7, 6, 9, 3, 2, 5]
duplicates = []

# Your code here

def ident_dupl(lst):
    duplicates = set()
    seen = set()
    for x in numbers:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return  list(duplicates)

duplicates = ident_dupl(duplicates)

print("Duplicate numbers:", duplicates)


# 9. Generate squares of numbers from 1 to 10
# Task: Create a list containing the squares of numbers from 1 to 10.


print("Task 9: Generate squares of numbers from 1 to 10")

numbers = list(range(1, 11))
squares = []

# Your code here

def squares_list(numbers):
    squares = []
    for x in numbers:
        squares.append(x ** 2)
    return squares

squares = squares_list(numbers)

print("Squares of numbers:", squares)
#
#
#
# # 10. Simple user database with dictionary
# # Task: Create a dictionary that stores usernames and passwords.
# # Add a new user, check if a user exists, and update a password.
#
#
# print("Task 10: Simple user database with dictionary")
#
# users = {
#     "admin": "1234",
#     "user1": "qwerty",
#     "guest": "guest123"
# }
#
# # Add a new user
# new_username = "new_user"
# new_password = "password123"
#
# # Your code here
#
# print("New user added:", users)
#
# # Check if a user exists
# check_username = "admin"
#
# # Your code here
#
# print(f"User {check_username} {'found' if exists else 'not found'}.")
#
# # Update a user's password
# change_username = "user1"
# new_pass = "new_secure_password"
#
# # Your code here
#
# print(f"Password for {change_username} updated:", users)
