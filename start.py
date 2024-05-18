def add_func(a, b):

    return a + b 

if __name__ == "__main__":
    print("Run")

def get_largest_num(numbers, n):

    numbers.sort()
    return numbers[-n:]

nums = [1,3,56,8,7,65,14,20]
print(f"numbers as it: {nums}")

#largest = get_largest_num(nums, 4  )
#print(f"the last sorted four largest numbers are:  {largest}")


def get_smallest_num(numbers, n):
    numbers.sort()
    return numbers[:n]

#smallest = get_smallest_num(nums, 3)
#print(f"the last sorted smallest three numbers are: {smallest}")







