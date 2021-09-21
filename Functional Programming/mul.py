
def multiply_by_2(list):
    for index,item in enumerate(list):
        item *= 2
        list[index] = item
    return list 

print(multiply_by_2([1,2,3]))       