# 1. Creating a Set
# Task: Write a function create_set(lst) that takes a list lst and returns a set containing unique elements.

def create_set(lst):
    return set(lst)
print("Task 1: Creating a Set")
print(create_set([1, 2, 3, 2, 1, 4]))  # Expected: {1, 2, 3, 4}
print("-" * 30)

# 2. Accessing Set Elements
# Task: Write a function check_element(s, elem) that checks if elem is in the set s and returns True or False.

def check_element(x, elem):
    for item in x:
        if item == elem:
            return True
    return False


x = {1, 2, 3, 4, 5}
print("Task 2: Accessing Set Elements")

print(check_element(x,3))  # Expected: True
print(check_element(x,10))  # Expected: False
print("-" * 30)

# 3. Adding Elements to a Set
# Task: Write a function add_elements(s, elements) that takes a set s and a list elements, adding all
# elements from the list to the set.

def add_elements(s, elements):
    return s.union(elements)

print("Task 3: Adding Elements to a Set")
s = {1, 2, 3}
print(add_elements(s, [3, 4, 5]))  # Expected: {1, 2, 3, 4, 5}
print("-" * 30)


# 4. Removing Elements from a Set
# Task: Write a function remove_elements(s, elements) that removes elements from s based
#  on the list elements. If an element is not in s, ignore it.

def remove_elements(s, elements):
    for x in elements: # Проходим по списку элементов
        s.discard(x) # Удаляем элемент, если он есть
    return s

print("Task 4: Removing Elements from a Set")
s = {1, 2, 3, 4, 5}
print(remove_elements(s, [2, 4, 6]))  # Expected: {1, 3, 5}
print("-" * 30)

# 5. Looping Through a Set
# Task: Write a function print_set(s) that prints all elements of a set s, one per line.

def print_set(s):
    for item in s:
        print(item)

print("Task 5: Looping Through a Set")
s = {10, 20, 30}
print_set(s)
# Expected output (order may vary):
# 10
# 20
# 30
print("-" * 30)


# 6. Union of Sets
# Task: Write a function union_sets(s1, s2) that returns the union of two sets.

def union_sets(s1, s2):
    return s1 | s2

print("Task 6: Union of Sets")
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(union_sets(s1, s2))  # Expected: {1, 2, 3, 4, 5}
print("-" * 30)


# 7. Intersection of Sets
# Task: Write a function intersection_sets(s1, s2) that returns the intersection of two sets.

def intersection_sets(s1, s2):
    return s1.intersection(s2)

print("Task 7: Intersection of Sets")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(intersection_sets(s1, s2))  # Expected: {3, 4}
print("-" * 30)


# 8. Difference of Sets
# Task: Write a function difference_sets(s1, s2) that returns the difference of s1 relative to s2.

def difference_sets(s1, s2):
    return s1 - s2


print("Task 8: Difference of Sets")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(difference_sets(s1, s2))  # Expected: {1, 2}
print("-" * 30)

# 9. Symmetric Difference of Sets
# Task: Write a function symmetric_difference_sets(s1, s2) that returns elements present in only one of the two sets.

def symmetric_difference_sets(s1, s2):
    return s1 ^ s2

print("Task 9: Symmetric Difference of Sets")
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(symmetric_difference_sets(s1,s2))


# 10. Checking if a Set is a Subset
# Task: Write a function is_subset(s1, s2) that checks if s1 is a subset of s2.

def is_subset(s1, s2):
    return s1 <= s2


print("Task 10: Checking if a Set is a Subset")
s1 = {1, 2}
s2 = {1, 2, 3, 4}
print(is_subset(s1, s2))  # Expected: True
print(is_subset(s2, s1))  # Expected: False
print("-" * 30)