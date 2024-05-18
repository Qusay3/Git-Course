name = "John"
count = 1

def another():
    color = "Blue"
    #count = 2
    #count += 1
    global count
    count += 1
    print(count)

    def greeting(firstname):
        nonlocal color
        color = "Red"
        print(color)
        print(name)
        print(firstname)

    greeting("Mallok")

another()