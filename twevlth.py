# Read 10 numbers from user and find the average of all.
# a) Use comparison operator to check how many numbers are less than average and print them
# b) Check how many numbers are more than average.
# c) How many are equal to average.

lst = []
b = 0
for i in range(0, 10):
    a = int(input("Enter 10 Numbers: "))
    lst.append(a)
    b += a

avg = b / len(lst)
cnt1 = cnt2 = 0

for i in lst:
    if i < avg:
        print(i, " is lesser than ", avg)
    elif i > avg:
        cnt1 = cnt1 + 1
    elif i == avg:
        cnt2 = cnt2 + 1
        
print(cnt1," numbers are greater than ", avg)

print(cnt2," numbers are Equal to  ", avg)
    









