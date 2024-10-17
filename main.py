#print("Hello World")

#variables
# Integer variable
age = 25
print(age )

# Float variable
height = 5.9
print(height)

# String variable
name = "Alice"
print(name)

# Boolean variable
is_student = True
print(is_student)

# Example usage
if is_student:
    print(f"{name} is {age} years old and is a student with a height of {height} feet.")
else:
    print(f"{name} is {age} years old and is not a student.")

#how to find data type
name="rimsha"
print(type(name))
#operators
a=10
b=5
print(a-b)
print(a+b)
print(a/b)
print(a*b)
print(a%b)
print(a**b)
#relational operator
a=10
b=11
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#assignment operator
x = 5
print("Initial x:", x)

# Using compound assignment operators
x += 3
print("After += 3:", x)  # Output: 8

x -= 2
print("After -= 2:", x)  # Output: 6

x *= 4
print("After *= 4:", x)  # Output: 24

x /= 3
print("After /= 3:", x)  # Output: 8.0

x //= 2
print("After //= 2:", x)  # Output: 4.0

x %= 3
print("After %= 3:", x)  # Output: 1.0

x **= 3
print("After **= 3:", x)  # Output: 1.0

#logical operators
x = 8
y = 15

# Using logical operators
if (x < 10 and y > 10):
    print("Both conditions are True.")

if (x < 5 or y > 10):
    print("At least one condition is True.")

if not (x == y):
    print("x is not equal to y.")

#type conversion
a=2
b=4.25
sum=a+b
print(sum)
#type casting
x = "10"
y = int(x)  # Converts string to integer
print(y)  # Output: 10

#input in python
name=input("enter name:")
age=input("enter age:")
marks=input("enter marks:")
print("welcome",name)
print("age=",age)
print("marks=",marks)

#practice work
#write a program to input 2 numbers & print their sum
first=int(input("enter first: "))
second=int(input("enter second: "))
print("sum=", first+second)
#wap to input side of a sequare&print its area
side=float(input("enter sequare side:"))
print("area=",side*side)
#wap to input 2 floating point numbers&print their average
a=int(input("enter first: "))
b=int(input("enter second: "))
print("avg=", (a+b)/2)
#wap to input 2 int numbers,a and b print true if a is greater then or equal to b.if not print else

a=int(input("enter first: "))
b=int(input("enter second: "))
print(a>=b)
