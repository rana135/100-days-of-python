thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)                  # apple banana cherry

for x in range(len(thislist)):
    print(thislist[x])        # apple banana cherrry

# Use the range() and len() functions to create a suitable iterable:
for x in range(5):
    print(x)        # 0 1 2 3 4

for x in range(len(thislist)):
    print(x)        # 0 1 2


# Print all items, using a while loop (condition এর উপর depened করে মূলত while loop কাজ করে) :
i = 0
while i < len(thislist):
    print(thislist[i])     # apple banana cherrry
    i = i + 1              # [এটি না দিলে infinite loop হয়ে যাবে]

