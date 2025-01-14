# Write a program in Python to compute the greatest common divisor and the least common multiple of two integers.
# Input two numbers
n1 = int(input("Enter First number: "))
n2 = int(input("Enter Second number: "))

x = n1
y = n2

while n2 != 0:
    t = n2
    n2 = n1 % n2
    n1 = t

gcd = n1
print("GCD of {0} and {1} = {2}".format(x, y, gcd))

lcm = (x * y) // gcd 
# Use integer division (//) to ensure LCM is an integer
print("LCM of {0} and {1} = {2}".format(x, y, lcm))
