
first = 'Qusay'
last = 'Ahmed'

multiline = ''' Hi, how is it going?
                        all good?

                               thanks!
'''

print(multiline)
print(multiline.title())
print(multiline.replace('good', 'ok'))

print(len(multiline))
multiline += "             "
multiline = "                          " + multiline
print(len(multiline))
print(len(multiline.strip()))  # remove unwanted characters
print(len(multiline.lstrip()))  # remove the spaces in left side
print(len(multiline.rstrip()))     # lest side


print("")  # empty lines

# build menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$4".rjust(4))
print("Cheescake".ljust(16, ".") + "$3".rjust(4))


print(" ")

# sring index  value
print(first[1])
print(first[-1])
print(first[0:-1])
print(first[1:])


# some method return boolean
print(first.startswith("Q"))
print(first.endswith("u"))


# Boolean data value
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
