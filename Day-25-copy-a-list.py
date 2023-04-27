# Make copy of a list with the copy() method (thislist থেকে copy করে mylist এ রাখবো):
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)       # ['apple', 'banana', 'cherry']

# Another way to make a copy is to use the built-in method list():
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)       # ['apple', 'banana', 'cherry']

# There are ways to make a copy:-
# 1/ copy ()
# 2/ list ()