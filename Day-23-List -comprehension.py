# comprehension দিয়ে যেকোন সংখ্যাকে squares করা:
numbers = [1,2,3,4,5]
squares = [number**2 for number in numbers]
print(squares)         # [1, 4, 9, 16, 25]

# উপরেরটাই just details এ করা হয়েছে:
squares = []
for number in numbers:
    squares.append(number**2)
print(squares)           # [1, 4, 9, 16, 25]

# comprehension দিয়ে যেকোন সংখ্যাকে Double করা:
double = [i*2 for i in numbers]
print(double)            # [2, 4, 6, 8, 10]

# comprehension দিয়ে যেকোন সংখ্্যার সাথে 5 করে যোগ করা:
increase = [i+5 for i in numbers]
print(increase)          # [6, 7, 8, 9, 10]
