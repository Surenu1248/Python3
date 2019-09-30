# Create a list of 5 names and check given name exist in the List.
#        a) Use membership operator (IN) to check the presence of an element.
#        b) Perform above task without using membership operator.
#        c) Print the elements of the list in reverse direction.

lst = ["Suresh", "Ramesh", "Raju", "Sampath", "Ravi"]
str1 = "Sampath"
a = True

# Checking name of the person  Using Memebership operator 
if str1 in lst:
    print(str1, "is presented in the exist list...")
else:
    print(str1, "is not presented in the existlist....")

# Checking name of the person without Memebership operator
for i in lst:
    if i == str1:
        a = True
        break
    else:
        a = False
if a == True:
    print(str1, "is presented in the existed list.....")
else:
    print(str1, "is not presented in the existed list...")

# printing the list in reverse direction
print("----------List in reverse direction----------")
print(lst[::-1])



