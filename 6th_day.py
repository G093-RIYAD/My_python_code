marks = int(input("Your markes in programming : "))

def your_grade (grade):
    print(f"You have got: {grade}")

if marks > 90 or marks < 40:
    print("your marks are vary good or bad.")
    if marks > 80:
        print("yor marks are good")
    else:
        print("Not so good!")
else:
    print("you are okay.")
#The boolian value.

the_user_number = 80 > 60
print(the_user_number)
the_user_number = 80 < 60
print(the_user_number)


number = int(input("Give a number:"))
the_user_number = number>= 80
pmassage = "The number is greater than or equals 80: " + str(the_user_number)
print(massage)

#Python Boolean

print(10>9)
print(299>3999)
print(899==90)

#Python Boolean with true value;

print(bool("yo What's up?"))
print(bool(79))
print(bool(["apple", "cherry", "banana"]))

#Python Boolean false value;

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


a = 980
b = 60

if b > a:
    print("b is grater than a")
else:
    print("b isn't grater than a")

    def even_num(number):
    if number % 2 == 0:
        return True
    else:
        return False

starting = 0
while starting < 1000:
    if even_num(starting):
        print(f"{starting} is Even")
    else:
        print(f"{starting} is Odd")
    starting = starting + 1

print("Finished")

