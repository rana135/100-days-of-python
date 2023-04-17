price = {10,25,65,15,2,39,255}
product = bytes(price)
# product[1] = 105   # (Error) 'bytes' object does not support item assignment
print(type(product))   # bytes

price = {10,25,65,15,2,39,255}
product = bytearray(price)
product[1] = 100
print(type(product))   # bytearray
print(product[1])   # 100
