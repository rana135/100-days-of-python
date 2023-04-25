# Access from list (Print the second item of the list) :-
thislist1 = ["apple", "banana", "cherry"]
print(thislist1[1])      # banana
print(thislist1);        # ['apple', 'banana', 'cherry']

# change list item
thislist1[0:2] = ["blackcurrant", "watermelon"]
print(thislist1)          # ['blackcurrant', 'watermelon', 'cherry']

thislist1[1] = "Mango"
print(thislist1)           # ['apple', 'Mango', 'cherry']

'''
Negative Indexing:-
-1 refers to the last item and -2 refers to the second last item
'''
print(thislist1[-1])     # cherry
print(thislist1[-2])     # Mango


# -----------------------------------------------------------------------------------------------
# specify a range of indexes by specifying where to start and where to end the range.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])    # ['cherry', 'orange', 'kiwi']

# শুরু থেকে আইটেমগুলিকে return করে এবং শেষ হয় যত পর্যন্ত দেওয়া থাকে:
print(thislist[:4])     # ['apple', 'banana', 'cherry', 'orange']

# 2 index থেকে শুরু করে last পর্যন্ত যাবে:
print(thislist[2:])     # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

# শেষের দিক থেকে 1 করে count করে এসে 4 পর্যন্ত count করলে যেই orange কে পাই সেটাই -4 এর মান যা থেকে শুরু করে -1 পর্যন্ত:-
print(thislist[-4:-1])  # ['orange', 'kiwi', 'melon']

# condition
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# The insert() method inserts an item at the specified index:
thislist3 = ["apple", "banana", "cherry"]
thislist3.insert(2, "watermelon")
print(thislist3)     # ['apple', 'banana', 'watermelon', 'cherry']
