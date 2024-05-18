import random

print("Welcome to our TestYourMath skills")
user_name = input("Enter Your Name: ")
print("Hi,", user_name)

score = 0

def test():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

# Loop for 5 rounds
for _ in range(5):
    operation = random.choice([addition, subtraction, multiplication, division])
    num1, num2 = test()
    result = operation(num1, num2)
    user_answer = float(input(f"What is {num1} {'+' if operation == addition else '-' if operation == subtraction else '*' if operation == multiplication else '/'} {num2}? "))
    if user_answer == result:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

print("Your final score is:", score)
