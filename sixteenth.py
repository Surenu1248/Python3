# Write program to perform following:
#     i) Check whether given number is prime or not.
#    ii) Generate all the prime numbers between 1 to N where N is given number.

# Checking the given number prime or not
a = 20#int(input("Enter the number to check prime number or not? : "))
def check_prime(a):
    for i in range(2, a//2):
        if(a % i == 0):
            return "Its not a prime Number...."
        else:
            return "Its prime Number..."
    
#print(check_prime(a))    

# Generating all the prime numbers in between range
b = int(input("Enter the starting position: "))
c = int(input("Enter the ending position: "))

d = []


def check_prime1():
    for i in range(b, c):
        for j in range(2, i//2):
            if(i % j == 0):
               # print("Not Prime")
                break
            else:
                d.append(i)
                break
    
    
print(check_prime(a))
check_prime1()
print("Prime numbers in between the given range: ")
print(d)





