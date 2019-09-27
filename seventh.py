# Create a list with at least 10 elements having integer values in it;
#       Print all elements
#       Perform slicing operations
#       Perform repetition with * operator
#       Perform concatenation with other list.

lst = [10,20,30,40,50,60,70,80,90,100,110]
lst2 = [11,22,33,44,55,66,77,88,99]

# Printing all Elements.....
print("List Elements are: ", lst)

# Slicing Operations.....
print("Slicing Operation: ", lst[3:6])

# Repetition.....
print("Repetition of list for 5 times: ", (lst,) * 5)

# Concatenation of lst and lst2 
print("Combination of lst and lst2: ", lst + lst2)
