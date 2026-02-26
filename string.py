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