def add_one(num):

    if (num >= 9):
        return num + 1
    
    total = num + 1
    print (total)

    return add_one(total)
    
#add_one(5)
mynewtotal = add_one(0)
print(mynewtotal)


def add_one(num):
    total = num
    for i in range(num, 10):
        total += 1
        print(total)
    return total

mynewtotal = add_one(0)
print(mynewtotal)


    
