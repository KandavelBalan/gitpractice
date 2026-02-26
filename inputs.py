
# a = int(input("enter the input a "))
# b = int(input("enter the input b "))

# print(a+b)



import sys

if len(sys.argv) == 2:
    print("usage: please the name")
    sys.exit()

full_name = " ".join(sys.argv[1:])

email = full_name.lower().replace(" ",".")+"@sde.com"

# print(full_name.lower().replace(" ","."))

print("\n the profile is created")
print("full_name is "+full_name)
print("email ID is "+email)