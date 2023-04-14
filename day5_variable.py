# Day:5--> Python Variable:-
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