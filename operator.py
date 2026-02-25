# x = 5
# y = 4

# #Arthimetic operators
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(x//y)

# #comparision

# print(x==y)
# print(x!=y)
# print(x > y)
# print(x < y)
# print(x+y)

# #logical

# a = True
# b = False

# print(a and b)
# print(a or b)
# print(not a)


# gst and discount calculation using comparison and arthmetic operator

amount =  1000
tax = amount * 0.18
total = amount + tax

print(total)


if total > 1000:
    discount = total * 0.10
    total -= discount

print(total)

# cinemas discount

age = 24
student = False

if age >= 60 or student == True:
    print("Yes eligible for discount")
else:
    print("Not eligible for the discount")
