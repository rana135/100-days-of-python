'''String Formatting:-
string এর ভিতর যদি কোন number যোগ/বিয়োগ/গুন/ভাগ করতে চাই তাহলে প্রথমে একটা f লিখে তারপর string("") ও {} এর ভিতরে কাজ করতে হবে।
'''
name= "Rana"
father = 100
mother = 500
print(f'My Name is {name} & Received Tk from parents {father + mother}')
print('Received from parents', father + mother) # Normally এভাবে করে থাকি।