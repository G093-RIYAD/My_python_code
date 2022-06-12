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
