# Write a program to find the number is Prime or not.

def prime(a):
    c = True
    for i in range(2, a // 2):
        if(a % i) == 0:
            c = False
            break
        else:
            c = True
        
    return c 


print(prime(11))
