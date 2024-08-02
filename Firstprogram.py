#Write a program to print twin primes less than 1000. if two consecutive odd numbers are both prime then they are known as twin primes.

def is_prime(n):
    for t in range(2,n):
      if n%t==0:
        return False
    return True
def generate_twins(start,end):
    for t in range(start,end):
      s=t+2
      if(is_prime(t)and is_prime(s)):
         print("{:d},{:d}".format(t,s))
generate_twins(2,1000)      
               
    