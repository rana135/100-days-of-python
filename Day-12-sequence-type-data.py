# Brackets Name:
'''
square brackets --> []
parentheses --> ()
curly brackets --> {}
'''

# এটি মূলত array এর মতো আর এটি Mutable(change করা যায়):
li = ["Rana","Anik","Joy","Jhanker"]
print(li)        # ['Rana', 'Anik', 'Joy', 'Jhanker']
print(type(li))  # list

# যেহেতু list Mutable তাই list এর value change করে দিতে পারি:
li[0] = "Shimul"
print(li)        # ['Shimul', 'Anik', 'Joy', 'Jhanker']


# tuple type data: (just ()bracket দিতে হবে আর বাকীটা list এর মতোই but এটি Immutable(change করা যায় না))
tup = (5, 10, 15, 20, 25)
print(tup)       # (5, 10, 15, 20, 25)
# tup[1] = 100   # TypeError: 'tuple' object does not support item assignment
print(tup)
print(type(tup)) # tuple


# range type data Example:
ran = range(4)
print(ran)         # range(0, 6)
print(type(ran))   # range

# for loop with range:-
for i in ran:
    print(i)       # 0 1 2 3

# Direct range লিখেও করা যাবে:
for i in range(8):
    print(i)       # 0 1 2 3 4 5 6 7


