marks = int(input("Your markes in programming : "))

def your_grade (grade):
    print(f"You have got: {grade}")

if marks >= 90:
    print("your mareks is excellent")
    if marks > 80:
        print("your are good")
elif marks <= 40:
    print("your isn't good")
else:
    print("you are okey")
