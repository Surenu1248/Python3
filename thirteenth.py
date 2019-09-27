# Write a program to find the biggest of 4 numbers.
#   a) Read 4 numbers from user using Input statement.
#   b) extend the above program to find the biggest of 5 numbers.
# (PS: Use IF and IF & Else, If and ELIf, and Nested IF)

a = int(input("Enter 'a' value: "))
b = int(input("Enter 'b' value: "))
c = int(input("Enter 'c' value: "))
d = int(input("Enter 'd' value: "))
e = int(input("Enter 'e' value: "))
max1 = a

if (a > b & a > c & a > d & a > e):
    max1 = a;
elif b > c & b > d & b > e:
    if max1 < b:
        max1 = b
elif c > d & c > e: 
    if max1 < c:
        max1 = c
elif d > e:
    if max1 < d:
        max1 = d
else:
    max1 = e


print(max1, " is Maximum number......")

