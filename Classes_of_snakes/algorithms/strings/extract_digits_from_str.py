def get_digits(s):
    digits = ""
    for i in s:
        if i.isdigit():
            digits += i

        
    return digits
print(get_digits("shfg43rer31"))