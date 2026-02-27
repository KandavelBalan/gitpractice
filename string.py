import sys

name = "kanDhu"

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(len(name))

mobile = "9922003321"
masked = mobile[:2] + "******" + mobile[-2:]
print(masked)


note = "welcome TO"
location = "kolatur, chennai"
formatted = f'{note.title()} {location.title()}'

print(formatted)

loc = "alandhur metro"
print(loc)
rep_loc = loc.replace("alandhur","st.thomas mount")
print(rep_loc)

msg = "the otp: 129876. please don't share it"
otp = msg.split(":")[1].split(".")[0].strip()
print(otp)

# promo_msg = "".join(sys.argv[1:])
# if "zomato" in promo_msg:
#     print("offer used")

feedback = "enter your feedback for the driver: the driver is polite and punctual"
print("position is",feedback.find("polite"))

fullname = "kandavel dhanabalan"
intials = "".join([word[0].upper() for word in fullname.split(" ")])
print(intials)


dirty_words = "   welcome to chennai   "
clean_word = dirty_words.strip()
print(clean_word)

word = "the driver is polite and punctual"
print(len(word.split(" ")))