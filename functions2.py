# def square(a,b,c,d):
#     area = (a+b)*(c+d)
#     return area

# result = square(4,6,8,9)
# print(result)
# ###########

# def sum2(num1, num2):
#     total = num1 + num2
#     return total
    
# total = sum2(1,6)
# print(total)
# ############

# def sum3(num1, num2):
#     print(num1 + num2)

# sum3(6, 10)
# sum3(4, 1)

# def add (num1, num2):
#     if (type(num1) is not int or type(num2) is not int):
#         return
#     return num1 + num2

# total = add("a", 20)  # will return none
# print(total)

# def add (num1, num2 = 5):
#     if (type(num1) is not int or type(num2) is not int):
#         return 
#     return num1 + num2

# total = add("20")  # will return none
# print(total)


def multiple_items(*args):
    print(args)
    print(type(args))   #tuple

multiple_items("Dave", "Sara", "John") 


def mult_name_items(**kwargs):
    print(kwargs)
    print(type(kwargs))  #dictionary

mult_name_items(first = "Dave", last = "John")