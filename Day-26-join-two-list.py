'''
There are several ways to join, or concatenate, two or more lists in Python:-
1/ '+' operator
2/ append()
3/ extend()  [One of the easiest ways]
'''

# Normal ways are by using the + operator:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)            # ['a', 'b', 'c', 1, 2, 3]

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)

print(list1)            # ['a', 'b', 'c', 1, 2, 3]

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)            # ['a', 'b', 'c', 1, 2, 3]
