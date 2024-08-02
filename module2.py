first = input("Enter First Number : ")
operator = input("Enterr Operator (+,-,/,*,%) : ")
second = input("Enter Second Number : ")

first = int(first)
second = int(second)

if operator == "+" :
    print (first + second)
elif operator == "-" :
    print (first - second)
elif operator == "/" :
    print (first / second)
elif operator == "*" :
    print (first * second)
elif operator == "%" :
    print (first % second)
else :
    print("Invalid Operator !!")


