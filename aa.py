def reserve_func(list):
    for i in range(len(list)):          
        temp = list[i]
        list[i-1] = temp
        print (list)

    return list
print(reserve_func([1,5]))

