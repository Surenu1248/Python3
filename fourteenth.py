# Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation
#     a) Print all names on to screen
#     b) Read the index from the  user and print the corresponding name from both list.
#     c) Print the names from 4th position to 9th position
#     d) Print all names from 3rd position till end of the list
#     e) Repeat list elements by specified number of times (N- times, where N is entered by user)
#     f)  Concatenate two lists and print the output.
#     g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

emp_no = [101,102,103,104,105,106,107,108,109,110]
emp_name = ["Sai", "Ramesh", "Ravi", "Ratna", "Swapna", "Roja", "Saroja", "Radha", "Gopika", "Suresh"]

# Printing all Employee names.....
for name in emp_name:
    print(name)

# Reading the index from user and printing the corresponding result from both list.....
a = int(input("Enter the index value from 0 to 9: "))
print("----------Your requested Employee Details are as follows----------")
print("Employee no is: ", emp_no[a])
print("Employee name is: ", emp_name[a])

# Printing the names from 4th Position to 9th
print("---------- Employee names from 4th position to 9th ----------")
print(emp_name[3:9])

# Printing the names from 3rd to till the end of the list
print("---------- Employee names from 3rd position to till last ----------")
print(emp_name[2:])

# Repeating the list elements by N times
n=int(input("Enter the number to repeat the list for N times: "))
print(n * (emp_name, " "))

# Concatenating the two lists 
print(emp_no + emp_name)

# Printing the both lists side by side order
for i in range(0, len(emp_no)):
    print(str(emp_no[i]) + " " + emp_name[i])




