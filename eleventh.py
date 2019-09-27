# Read 2 numbers to variable a and b and perform all bitwise operations on that numbers.

a = int(input("Enter 'a' value:  "))
b = int(input("Enter 'b' value: "))

print("AND operation of a and b: ", a & b)

print("OR operation of a and b: ", a | b)

print("XOR operation of a and b: ", a ^ b)

print("Ones Complement operation of a: ", ~ a)

print("Ones Complement operation of b: ", ~ b)

print("Binalry left shift operation of a and b: ", a << b)

print("Binary right shift operation of a and b: ", a >> b)
