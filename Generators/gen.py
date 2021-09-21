

def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(1000)
next(g)
next(g)
next(g)
print(next(g))

# for item in generator_function(1000):
#     print(item)        

# def make_list(num):
#     result=[]
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list = make_list(100)   


