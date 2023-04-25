'''
Arithmetic কাজগুলোকে কোন একটা variable এর মধ্যে assign করে রাখার মাধ্যমে mathmatical কোন কাজ করি
তখন তাকে assignment operator বলে।
'''

# Assignment Operator:
x = 10
x += 3    # Same As : x = x + 3
print(x)  # 13

y = 10
y -= 3    # Same As : y = y - 3
print(y)  # 7

x = 5
x *= 3    # Same As : x = x * 3
print(x)  # 15

x = 5
x /= 3    # Same As : x = x / 3
print(x)  # 1.6666666666666667

x = 5
x %= 3    # Same As : x = x % 3
print(x)  # 2

x = 5
x **= 3   # Same As : x = x ** 3
print(x)  # 125


# Comparison Operator:
x = 5
y = 3
print(x == y)   # False
print(x != y)   # True
print(x > y)    # True
print(x < y)    # False
print(x >= y)   # True
print(x <= y)   # False


# Python Logical Operators
print(x > 3 and x < 10)         # True
print(x < 5 or x < 4)           # False
print(not(x < 5 and x < 10))    # True