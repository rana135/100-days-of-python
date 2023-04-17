# Binary Types:	bytes, bytearray, memoryview
'''
যার মধ্যে bytes হচ্ছে immutable(যাকে change করা যাবে না) আর bytearray হচ্ছে mutable(change করা যাবে) ।
byte ও byttearray এর range হচ্ছে (0-256)
অর্থাৎ এই range এর মধ্যেই আমাদের সংখ্যাগুলো নিতে হবে।
যেহেতু 0 থেকে শুরু তাই 255 পর্যন্ত নিতে পারবো।
'''

price = {10,25,65,15,2,39,255}
product = bytes(price)
# product[1] = 105   # (Error) 'bytes' object does not support item assignment
print(type(product))   # bytes

price = {10,25,65,15,2,39,255}
product = bytearray(price)
product[1] = 100
print(type(product))   # bytearray
print(product[1])   # 100
