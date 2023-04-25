'''
list এ 2 ভাবে আমরা item add করতে পারি:
    1/append()
    2/insert()
'''

# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)   # ['apple', 'banana', 'cherry', 'orange']

# The insert() method inserts an item at the specified index:
thislist.insert(2, "watermelon")
print(thislist)   # ['apple', 'banana', 'watermelon', 'cherry', 'orange']