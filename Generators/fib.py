def fib(number):
    f0 = 0
    f1 = 1
    for i in range(number):
        yield f0
        temp = f0 + f1
        f0 = f1
        f1 = temp

for item in fib(8):
    print(item)        


        
        
