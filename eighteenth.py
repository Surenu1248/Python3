# Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 
# (reverse printing)
# a) By using For loop 
# b) By using while loop
# c) Let mystring ="Hello world"
n = 100
lst1 = []
lst2 = []
lst3 = []
lst4 = []

# Using for Loop
for i in range(1, n):
    #print(i)
    lst1.append(i)
    lst2.append(n-1)
    #print(n-1)
    n=n-1
print("-----------Numbers from 1 to 100-----------")
print(lst1)

print("------------Numbers from 1 to 100 in reverse order-----------")
print(lst2)

# Using while Loop
n = 100
print("------------Using While Loop-----------")
while n > 0:
    #print(n)
    lst3.append(n)
    lst4.append(n - 1)
    n=n - 1
    
print(lst3)
print("------------In reverse order----------- ")
print(lst4)

# printing each character in seperate line
str1 = "Hello world"
str1.split()
for i in str1:
    print(i)











