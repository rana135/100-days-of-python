'''
Python has a set of built-in methods that you can use on lists:-
    append()	Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()	    Returns a copy of the list
    count()	    Returns the number of elements with the specified value
    extend()	Add list2 at the end of list1
    index()	    Returns the index of the first element with the specified value
    insert()	Adds an element at the specified position
    pop()	    Removes the element at the specified position
    remove()	Removes the item with the specified value
    reverse()	Reverses the order of the list
    sort()	    Sorts the list
'''


# Add an element to the fruits list:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)       # ['apple', 'banana', 'cherry', 'orange']

# Remove all elements from the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)       # []

# Copy the fruits list:
fruits = ["apple", "banana", "cherry"]
x = fruits.copy()
print(x)            # ['apple', 'banana', 'cherry']

# cherry টা কতবার আছে তা count করবে:
fruits = ["apple", "banana", "cherry", "cherry"]
x = fruits.count("cherry")
print(x)            # 2

# Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)       # ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)            # 2

# Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)       # ['apple', 'orange', 'banana', 'cherry']

# Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)       # ['apple', 'cherry']

# Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)       # ['apple', 'cherry']

# Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)       # ['cherry', 'banana', 'apple']

# Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)         # ['BMW', 'Ford', 'Volvo']

