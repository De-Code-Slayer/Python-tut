def largerthan(num,comp):
    if num == "" or comp == "":
        return False
    if len(num) > len(comp) and num[0] != "0":
        return True
    elif len(num) == len(comp):
        for i in range(len(num)):
            c = num[i]
            h = comp[i]
            if c < h:
                return False
        if num[-1] == comp[-1]:
            return False
        return True

print(largerthan("112","111"))
        