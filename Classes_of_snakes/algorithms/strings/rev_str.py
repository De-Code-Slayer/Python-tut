def are_rev(a,s):

    if len(a) == len(s):
        for i in range(len(s)):
            num = (len(s)-(i+1))
            if a[i] == s[num]:
                return True
            else:
                return False
    else:
        return False   
    return False          

print(are_rev("",""))