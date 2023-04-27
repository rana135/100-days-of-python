# Use the add method to add "orange" to the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)           # {'orange', 'banana', 'cherry', 'apple'}

# Check if "apple" is present in the fruits set:
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes")          # Yes

# Use the correct method to add multiple items (more_fruits) to the fruits set:
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)           # {'mango', 'cherry', 'apple', 'banana', 'grapes', 'orange'}

# Use the remove method to remove "banana" from the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)           # {'apple', 'cherry'}

# Use the discard method to remove "banana" from the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)           # {'apple', 'cherry'}
