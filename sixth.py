# Write a program to read string and print each character separately.
#    a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
#    b) Repeat the string 100 times using repeat operator *
#    c) Read string 2 and concatenate with other string using + operator.


# Printing the String in Seperate line.....

str1 = "Welcome to Wipro"
for i in range(0, len(str1)):
    print(str1[i], '\n')

    
# Slicing the String to generate substring.....

str2 = "Welcome to Wipro Technologies....."

print(str2[0 : 7])
print(str2[11 : 16])
print(str2[17 : ])


# Printing the String for 100 times.....

str3 = "Wipro"

print(100 * (str3 + " "))


# Reading two string and concatinating them to single string.....

str4 = input("Enter the First String:  ")
str5 = input("Enter the Second String:  ")

print(str4 + str5) 
