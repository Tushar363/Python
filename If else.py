a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
sum_a = 0
sum_b = 0
for div in range(1, a):
    if(a%div == 0):
        sum_a=sum_a+div
for div2 in range(1,b):
    if(b%div2 == 0):
        sum_b=sum_b+div2
if(sum_a==b and sum_b==a):
    print("Yes the number is amicable")
else:
    print("No the number is not amicable")


