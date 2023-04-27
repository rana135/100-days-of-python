'''
Tuple(টাপল) শুরু হয় () bracket দিয়ে আর এর data কে change করা যায় না। এটি list থ
েকে tuple এর different আর এছাড়া বাকী সব প্রায় একই।
'''

thistuple = ("apple", "banana", "cherry", "apple", "cherry", False, 1)
print(thistuple)                # ('apple', 'banana', 'cherry', 'apple', 'cherry', False, 1)
print(type(thistuple))          # tuple

# many items a tuple has, use the len() function:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))           # 3

# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])             # banana
# thistuple[1] = "Mango"          # TypeError: 'tuple' object does not support item assignment

# Negative index এর সময় last এর item থেকে access নিতে হবে আর তা count 0 থেকে না হয়ে 1 থেকে হবে:-
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])            # cherry


# (:)দিয়ে লিখলে তাহলে last item টাকে বাদ দিয়ে count করা হয়। তাই যদি item 5 টা থাকে
# আর যদি সবগুলোকে access করতে চাই তাহলে আমাাদেরকে 6 দিয়ে নিতে হবে। কারন সর্বদা সে 1 টা কম পেয়ে থাকে।
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])           # ('cherry', 'orange', 'kiwi')

# 0 থেকে Start হবে আর তা শেষ হবে 3 নং index এ গিয়ে:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])            # ('apple', 'banana', 'cherry', 'orange')

# 2 index থেকে start হয়ে তা একদম শেষ পর্যন্ত গিয়ে থামবে:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])            # ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# last থৈকে count শুরু করে তা 4 পর্যন্ত count করে সেখান থেকৈ শুরু করে -1 অর্থাৎ শেষেরটা কিন্তু এখানে শেষেরটার আগেরটা নিবো:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])         # ('orange', 'kiwi', 'melon')

