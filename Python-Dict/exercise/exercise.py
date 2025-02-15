
# 1. Accessing Dictionary Items
# Task: Write a function get_value(d, key) that returns the value associated
# with key in the dictionary d. If the key is not found, return "Key not found".

def get_value(d, key):
    if key not in d:
        return "Key not found"
    else:
        return d[key]

# def get_value(d, key):
#     return d.get(key, "Key not found") - сокращенная версия/более оптимальная



print("Task 1: Accessing Dictionary Items")
data = {"name": "Alice", "age": 25, "city": "New York"}
print(get_value(data, "age"))  # Expected: 25
print(get_value(data, "country"))  # Expected: Key not found
print("-" * 30)




# 2. Changing Dictionary Items
# Task: Write a function update_value(d, key, new_value) that updates the value
# of key in d. If the key doesn't exist, return "Key not found".

def update_value(d, key, new_value):
    if key in d:
        d[key] = new_value
        return d
    else:
        return "Key not found"


print("Task 2: Changing Dictionary Items")
data = {"name": "Alice", "age": 25}
print(update_value(data, "age", 30))  # Expected: {'name': 'Alice', 'age': 30}
print(update_value(data, "country", "USA"))  # Expected: Key not found
print("-" * 30)

# 3. Adding Items to a Dictionary
# Task: Write a function add_item(d, key, value) that adds a new key-value pair to d.

def add_item(d, key, value):
    if (key,value) not in d:
        d.update({key:value})
        return d


print("Task 3: Adding Items to a Dictionary")
data = {"name": "Alice", "age": 25}
print(add_item(data, "city", "New York"))  # Expected: {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("-" * 30)


# 4. Removing Items from a Dictionary
# Task: Write a function remove_item(d, key) that removes key from d. If key is not found, return "Key not found".

def remove_item(d, key):
    if key in d:
        d.pop(key)
        return d
    else:
        return "Key not found"

print("Task 4: Removing Items from a Dictionary")
data = {"name": "Alice", "age": 25}
print(remove_item(data, "age"))  # Expected: {'name': 'Alice'}
print(remove_item(data, "city"))  # Expected: Key not found
print("-" * 30)


# 5. Looping Through a Dictionary
# Task: Write a function loop_dict(d) that prints each key-value pair in d on a new line in the format "key: value".

def loop_dict(d):
    for key, value in d.items():
        print(key + ":" ,value)



print("Task 5: Looping Through a Dictionary")
data = {"name": "Alice", "age": 25, "city": "New York"}
loop_dict(data)
# Expected output:
# name: Alice
# age: 25
# city: New York
print("-" * 30)


# 6. Copying a Dictionary
# Task: Write a function copy_dict(d) that returns a copy of dictionary d.

def copy_dict(d):
    return d.copy()


print("Task 6: Copying a Dictionary")
data = {"name": "Alice", "age": 25}
new_data = copy_dict(data)
print(new_data)  # Expected: {'name': 'Alice', 'age': 25}
print(new_data is not data)  # Expected: True (should be a new object)
print("-" * 30)


# 7. Nested Dictionaries
# Task: Write a function get_nested_value(d, key1, key2) that returns the value stored in d[key1][key2].
# If a key is missing, return "Key not found".

def get_nested_value(d, key1, key2):
    if key1 in d and key2 in d[key1]:
        return d[key1][key2]
    else:
        return "Key not found"

print("Task 7: Nested Dictionaries")
data = {
    "user": {
        "name": "Alice",
        "age": 25
    }
}
print(get_nested_value(data, "user", "name"))  # Expected: Alice
print(get_nested_value(data, "user", "city"))  # Expected: Key not found
print("-" * 30)


# 8. Dictionary Methods: Keys, Values, Items
# Task: Write a function dict_methods(d) that returns a tuple containing three lists:
# all keys, all values, and all key-value pairs.

def dict_methods(d):
        keys = list(d.keys())
        values = list(d.values())
        key_values = list(d.items())
        return keys,values,key_values


print("Task 8: Dictionary Methods")
data = {"name": "Alice", "age": 25}
print(dict_methods(data))
# Expected: (['name', 'age'], ['Alice', 25], [('name', 'Alice'), ('age', 25)])
print("-" * 30)


# 9. Merging Two Dictionaries
# Task: Write a function merge_dicts(d1, d2) that merges d2 into d1 and returns the updated dictionary.

def merge_dicts(d1, d2):
    d1.update(d2)
    return d1

print("Task 9: Merging Two Dictionaries")
d1 = {"name": "Alice", "age": 25}
d2 = {"city": "New York", "age": 30}
print(merge_dicts(d1, d2))
# Expected: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print("-" * 30)

#
# 10. Checking if a Key Exists
# Task: Write a function key_exists(d, key) that returns True if key is in d, otherwise False.

def key_exists(d, key):
    if key in d:
        return True
    else:
        return False

# simplified version
# def key_exists(d, key):
#     return key in d  # Directly return the boolean result


print("Task 10: Checking if a Key Exists")
data = {"name": "Alice", "age": 25}
print(key_exists(data, "name"))  # Expected: True
print(key_exists(data, "city"))  # Expected: False
print("-" * 30)