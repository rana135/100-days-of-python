# Sort the list alphabetically:
thislist = ["b", "d", "c", "f", "a", "e"]
thislist.sort()
print(thislist)     # ['a', 'b', 'c', 'd', 'e', 'f']

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)     # [23, 50, 65, 82, 100]

# Sort the list descending:
thislist = ["b", "d", "c", "f", "a", "e"]
thislist.sort(reverse = True)
print(thislist)     # ['f', 'e', 'd', 'c', 'b', 'a']

# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)  # first এ সবগুলোকে ছোট হাতের করে নিলাম।
print(thislist)     # ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse the order of the list items (last থেকে first এর দিকে reverse হবে):
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)     # ['cherry', 'Kiwi', 'Orange', 'banana']


