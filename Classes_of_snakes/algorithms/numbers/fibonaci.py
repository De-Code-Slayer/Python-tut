def fib(num):
    if num == 1:
        return 1
    if num:
        return fib(num -1)+fib(num-2)
    return 0



for i in range(100):
    print(fib(i))