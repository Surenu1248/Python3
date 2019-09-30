# Using loop structures print even numbers between 1 to 100.  
# a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
#    i) Break the loop if the value is 50
#    ii) Use continue for the values 10,20,30,40,50
# b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
#      i) Break the loop if the value is 90
#      ii) Use continue for the values 60,70,80,90

lst1 = [10, 20, 30, 40, 50]
lst2 = [60, 70 ,80 ,90]

# a) Breaking the loop if the value is 50
print(" -----------Breaking the loop if the value is 50------------")
for i in range(1, 100):
    if i % 2 == 0:
        if i == 50:
            break
        else:
            print(i)


# b) continue the loop if 10, 20, 30, 40 ,50
print("-----------Continue the loop if 10, 20, 30, 40 ,50------------")
for i in range(1, 100):
    if i % 2 == 0:
        if i in lst1:
            continue
        else:
            print(i)
            
# a) Breaking the loop if the value is 90
print(" -----------Breaking the loop if the value is 90------------")
for i in range(1, 100):
    if i % 2 == 0:
        if i == 90:
            break
        else:
            print(i)


# b) Continue the loop if 60, 70, 80 ,90
print("-----------Continue the loop if 60, 70, 80, 90------------")
for i in range(1, 100):
    if i % 2 == 0:
        if i in lst2:
            continue
        else:
            print(i)
            
            
            
            

            
            
