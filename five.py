# Write a program to receive 5 command line arguments and print each argument separately.
# Example: >> python test.py arg1 arg2 arg3 arg4 arg5
# a) From the above statement your program should receive arguments and print them each of them. 
# b) Find the biggest of three numbers, where three numbers are passed as command line arguments.


import sys

s = []

for i in range(0, len(sys.argv)):
    s.append(sys.argv[i])
    print(s[i], '\n')

    
if s[1] > s[2]:
    print(s[1], " is Biggest Number......")
elif s[2] > s[3]:
    print(s[2], " is Biggest Number......")
else:
    print(s[3], " is Biggest number......")
    
