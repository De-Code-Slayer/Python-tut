def func(list,value):
    hash = dict()
    for i in list:
        val = value - i
        if val in hash:
            print(val,i)
            break
        else:
            hash[i] = 1
        

func([4,8,7,5,9],10)