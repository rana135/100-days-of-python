# list একটা single variable কিন্তু এর মধ্যে multiple item add করতে পারবো। যা কিনা Mutable এবং এটি যেকোন data type এর হতে পারে।

thislist = ["apple", "banana", "cherry"]
print(len(thislist))           # 3
print(thislist)                # ['apple', 'banana', 'cherry']
print(type(thislist))          # list

list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list2)                   # [1, 5, 7, 9, 3]
print(list3)                   # [True, False, False]

# আরেকভাবেও list create করা যায়:
thislist = list(("apple", "banana", "cherry"))
print(thislist)                # ['apple', 'banana', 'cherry']
