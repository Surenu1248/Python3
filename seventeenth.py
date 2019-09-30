# Write program to find the biggest and Smallest of N numbers.
#      PS: Use the functions to find biggest and smallest numbers. 

n = int(input("Enter the number: "))
lst1 = []
for i in range(0,n):
    a=int(input("Enter the numbers into the list: "))
    lst1.append(a)
    

# Finding the smallest number 
print("The smallest number in the given list: ", min(lst1))

# Finding the biggest number
print("The Biggest number in the given list:  ", max(lst1))
