# The remove() method removes the specified item (যাকে remove করতে চাই তার নাম টা বলে দিবো):
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)             # ['apple', 'cherry']

# The pop() method removes the specified index (াকে remove করতে চাই তার index টা বলে দিবো):
thislist.pop(1)
print(thislist)             # ['apple', 'cherry']

# কোন index না দিয়ে শুধু pop function কে কল করলে তাহলে last item হতে remove হওয়া শুরু করবে:
thislist.pop()
print(thislist)             # ['apple', 'banana']

# The del keyword also removes the specified index:
newlist = ["apple", "banana", "cherry"]
del newlist[0]
print(newlist)              # ['banana', 'cherry']

# The clear() method empties the list.
newlist.clear()
print(newlist)              # []
