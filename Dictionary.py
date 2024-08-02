#Creating a dictionary as "a"
a ={}
#"input" is used for taking the input from the user.
n = int(input("Number of elements:"))
#"Range" is used to return a sequence of number.
#"i" is a local variable
for i in range(n):
    t=input("Enter Key: ")
    s=input("Enter the value: ")
#"update" command is used to update.  
    a.update({t:s})
    print(a)
