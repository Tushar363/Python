def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
        return True
def generating_twins(start,end):
    for i in range(start,end):
        s = 2+i
        if (is_prime(i) and is_prime(s)):
            print(i,s)
generating_twins(2,1000)

t = int(input("Enter the first number: "))
s = int(input("Enter the second number: "))
Sum1 = 0
Sum2 = 0
for i in range(1,t):
    if t%i == 0:
        Sum1  =  Sum1 + i
for j in range(1,s):
    if s%j == 0:
        Sum2 =  Sum2 + j 
if(Sum1 == s and Sum2 == t):
    print("Amicable!")
else:
    print("Not Amicable!")                   

a = { }
n = int(input("Number of Elements: "))
for i in range(n):
    t = input("Enter Key: ")
    s = input("Enter Value: ")
    a.update({t:s}) 
    print(a)
                    
class student():
    def getstudentdetails(self):
        self.rollno =int(input("Enter the roll no: "))
        self.name = input("Enter the name: ")
        self.classofstudent = input("Enter the class: ")
    def getdetails(self):
        print(self.rollno)
        print(self.name)
        print(self.classofstudent)
S1 = student()  
S1.getstudentdetails()
print("results: ")
S1.getdetails()      

import numpy as np
arr =np.array([[1,2,3,4],[5,6,7,8]])
arr[:,[0,1]]=arr[:,[1,0]]

#temp=np.copy(arr[:,0])
#arr [:,0] = arr [:,1]
#arr [:,1] = temp
print(arr)

import numpy as np
import matplotlib.pyplot as plt

y = ([20,50,20,70,35])
x = (["a", "b", "c", "d", "e"])
plt.bar(x, y)
plt.show()

import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
data = np.random.randint(low =1, high =100, size =(10,10))
print("The data to br plotted:\n")
print(data)
hm = sn.heatmap(data = data)
plt.show()
