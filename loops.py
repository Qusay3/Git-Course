# value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1


# value = 1
# while value <= 10:
#     value += 1 
#     if value == 5:
#         continue
#     print(value)

# else:
#     print("value is now equal to: " + str(value))

# names = ["Dave", "Sara", "Anthony"]
# for name in names:
#     print(name)

# for i in "Mississippi":
#     print(i)

# for x in names:
#     if x == "Sara":
#         break 
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue 
#     print(x)

# for item in range(4):
#     print (item)

# for item in range(2, 7):
#     print (item)

# for item in range(0, 100, 5):
#     print (item)

# for item in range(5, 101, 5):
#     print (item)
# else:
#     print("Glsd that\s over!")


# names = ["Dave", "Sara", "Anthony"]
# actions = ["Codes", "Eats", "Sleeps"]

# for name in names:            # outer loop
#     for action in actions:
#         print(name + " " + action + ".")

names = ["Dave", "Sara", "Anthony"]
actions = ["Codes", "Eats", "Sleeps"]

for action in actions:            # outer loop
    for name in names:
        print(name + " " + action + ".")




'''
for i in range(10):
    print (i)
# range(start, stop, step)
# range (stop)
range (start, stop)

'''

'''
x = [2,3,6,9,8,7,23,95,595]
for i, element in enumreate(x):
    print(i, element)
# print the items with its index

'''

# Slicing
'''
x = [1,3,5,8,9,14,20,69,7,100]
y = ['hi', 'hello', 'cool', 'how are you', 'turkey']
z = 'monday'

sliced = [start:stop:step]
sliced = x[0,5,2]  # these are indexes
sliced = [:stop]
sliced = x[2:]      # [start:]    
scliced = x[::-1] # revere a list      
scliced = s[::-1] # revere a string as well             
woeks same with tuples too      
print(sliced)


'''

# set

'''
Only in situations if u care something exist ot not regardless its order or index
x = set()
s = {1,5,2,2}
s2 = {6,3,6,4,2}
x.add(5)
x.remove()
print(type({}))
print (2 in x)
print (33 in x)
print(s.union(s2))
print(s.difference(s2))
print(s.intersection(s2))

'''

# dict

'''
x = {'key': 4}
x['key2'] = 5
x[2] = [4,5,6]
print(x)
print('key' in x)
print(x.values())
print(x.keys())
del x['key']

to loop

for key, value in x.items():
    print(key, values)

    
for key in x:
    print(key, x[key])
        
'''


# comperhensions

'''
x = [x for x in range(5)]
x = [x + 5 for x in range(5)]
x = [0 for x in range(100)] for x in range(5)
x = [i for i in range(100) if i% 5 == 0]
x = {i:0 for i in range(100) if i% 5 == 0}  # works in dict as well
x = tuple(i for i in range(100) if i% 5 == 0) # works in tuples as well

print(x)

'''