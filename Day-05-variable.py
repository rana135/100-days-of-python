# Variable হচ্ছে একটা Container যেটার ভিতর information store করে রাখতে পারি, delete করতে পরি বা update করতে পারি।

# 1) string
name = 'Rana'
print ('my name is' +' ' +name )
print (type (name ))   # str

# 2) integer
age = 23
print ('my age is',str(age) )
print (type(age))   # int

# 3) floating
height = 170.18
print ('my height is',height, 'cm' )
print (type(height ))   # float

# 4)bollean
tf=True
print ('I love coding:',tf)
print (type (tf))   # bool

name, age ,height = 'Rana',23,170.18
print (name,age,height )
x=y=z=4
print (x+y+z)  # 12

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x+' '+y+' '+z)   # apple banana cherry

x = 5
y = "John"
print(x + y)   # TypeError: unsupported operand

