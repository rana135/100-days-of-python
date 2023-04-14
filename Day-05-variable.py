# Variable হচ্ছে একটা Container যেটার ভিতর information store করে রাখতে পারি, delete করতে পরি বা update করতে পারি।

# 1) string
name = 'Rana'
print ('my name is' +' ' +name )
print (type (name ))

# 2) integer
age = 23
print ('my age is',str(age) )
print (type(age))

# 3) floating
height = 170.18
print ('my height is',height, 'cm' )
print (type(height ))

# 4)bollean
tf=True
print ('I love coding:',tf)
print (type (tf))

name, age ,height = 'Rana',23,170.18
print (name,age,height )
x=y=z=4
print (x+y+z)  # 12

'''
Output:-
my name is Rana
<class 'str'>
my age is 23
<class 'int'>
my height is 170.18 cm
<class 'float'>
I love coding: True
<class 'bool'>
Rana 23 170.18
12
'''