t = int(input('Enter number 1: '))
s = int(input('Enter number 2: '))
sum1 = 0
sum2 = 0
for i in range(1,t):
    if t%i==0:
        sum1+=i
for j in range(1,s):
    if s%j==0:
        sum2+=j
if(sum1==s and sum2==t):
    print('Amicable!')
else:
    print('Not Amicable!')  