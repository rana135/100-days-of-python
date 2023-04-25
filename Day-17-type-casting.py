'''
একটা data type থেকে অন্য একটা data type এ dynamically convert করা। আর সেটি করার সময় যে function টি
ব্যবহার করা হবে সেটিকে type casting বলা হয়।
'''

'''
python is therefore done using constructor functions:
int()
float()
str()
'''

# str to int convert:-
num1 = '123456'
print(type(num1))       # str
print(type(int(num1)))  # int

# int to float convert:-
x = 2
print(type(x))          # int
print(type(float(x)))   # float

# float to str convert:-
y = 3.0
z = str(y)
print(type(y))          # float
print(type(z))          # str
