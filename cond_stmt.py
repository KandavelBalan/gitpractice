# age =  int(input("enter the age"))

# if age >= 18:
#     print("you're eligible to vote")
# else:
#     print("you're not eligible to vote")

# marks = int(input("enter the marks"))

# if marks >= 90:
#     if marks > 100:
#         print('please check the number')
#     else:
#         print("Grade A")
# elif marks >= 70:
#     print("Grade B")
# elif marks >= 50:
#     print("Grade C")
# else:
#     print("Grade F")

age = 20
driver_lic = False

if age >=18:
    if driver_lic == True:
        print("you're allowed to drive")
    else:
        print("Please get a lic")
else:
    print("seat in the back seat")


marks = 70
attendance = 70

if marks >= 50 and attendance >= 70:
    print("You're allowed to appear for the exam")
else:
    print("You're not allowed")

order_amount = 1000
days = 'sat'
member = False

if order_amount >= 1000 and days in ['sat','sun'] or member == True:
    print("20% discount")
    