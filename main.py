"""The target of this exercise is to create a string, an integer,
and a floating point number. The string should be named mystring and should contain the word "hello".
The floating point number should be named myfloat and should contain the number 10.0,
and the integer should be named myint and should contain the number 20."""

hello = "hello".upper()
print(hello)
print(hello.capitalize())
print (hello.lower().count('LL'))
print (hello.lower().count('l'))

number: int = 10
weather: str = 'sunny'
element: dict[int, str] = {1 : "hello", 2 : "name"}
nums : list[str] = ['6','5','9']

print(number)

def get_data() -> dict[str, int]:
    return {"a" : 1, "b" : 2}

def greet_people(people: list[str]) -> None:
    for person in people:
        print(f'Hello {person.capitalize()}!')

greet_people("Bob")


