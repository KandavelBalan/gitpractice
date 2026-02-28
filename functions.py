def add(*args):
    c= 0
    for num in args:
        c +=num
    return c

result = add(5,7,8)

print(result)



def details(**kwargs):
    out =''
    for key,value in kwargs.items():
         out += f' {key}: {value}'
    return out


sample = details(user_name ='kandavel', age = 31) 

print(sample)