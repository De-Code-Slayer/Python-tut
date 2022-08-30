# print list in reverse order

l = [1,5,8,6,9,7,4,3]
print(l[::-1])

def rev_list(l):
    s = 0
    e = len(l)-1
    while s < e:
        l[s],l[e] = l[e],l[s]
        s += 1
        e -= 1
    return l
print(rev_list([0,1,2,3,4,5,6,7,8,9,10]))

