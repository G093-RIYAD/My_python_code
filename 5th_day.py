#Python Conditions and (If,Else and Elif) statements.....

a = 50 
b = 45
if a > b :
    print("a is greater than b")
samm = 2093
max = 2333
if max > samm:
    print("samm id no. is greater then max")

a = 33
b = 33
if a > b:
    print("a is greater than b")
elif a == b:
    print("a and b are equal")

a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")


marks = int(input("Your markes in programming : "))

def your_grade (grade):
    print(f"You have got: {grade}")

if marks >= 90:
    your_grade("Golden A+")
elif marks < 90 and marks >= 80 :
    your_grade("A+")
elif marks < 80 and marks >= 70 :
    your_grade("A")
elif marks < 70 and marks >= 60 : 
    your_grade("A-")
elif marks < 60 and marks >= 50 : 
    your_grade("B")
elif marks < 50 and marks >= 40 : 
    your_grade("C")
elif marks < 40 and marks >33 : 
    your_grade("D")
elif marks >= 33:
    print("You Got passed SOMEHOW")
else:
    print("You have Failled")
