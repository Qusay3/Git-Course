# --------------------------
# Packing in puthon
# -----------------------



# print(1, 2, 3, 4)
# myList = [1,2,3,4]
# print(myList)
# print(*myList)

# def say_hello(n1, n2, n3, n4):
#     peoples = [n1, n2, n3, n4]
#     for name in peoples:
#         print(f"hello {name}")

# say_hello("qusay", "mohammed", "bakhit", "ahmed")

# def say_hello(*peoples): # n1, n2, n3, ...
  
#     for name in peoples:
#         print(f"hello {name}")

# say_hello("qusay", "abdo")

# def show_details(name, *skills):          #skill1, skill2, skill3, ...
#     print("Hello {name} your skills is: ")

#     for skill in skills :

#         print(skill)

# show_details("Qusay", "HTML", "CSS", "JS")
# show_details("Abdo", "HTML", "CSS", "JS", "PHP", "Python","Mysql", "Data Science")




# --------------------------
# -Function Default Prameters
# -----------------------

# def say_hello(name, age = "Unknown", country="Unknown"):          # default valur should be last parameter
#    print(f"hello {name} your age is {age} and your country is {country}")

# say_hello("Qusay", 30, "Canada")
# say_hello("Abdo", 28, "KSA")
# say_hello("Manhal", 28)
# say_hello("Ahmed")


# ---------------------------------------------------
# -- Function Packing, unpacking arguments **KWArgs --
# ---------------------------------------------------


# def show_skills(*skills) :
#     print(type(skills))
#     for skill in skills :
#           print(f"{skill}")
    
# show_skills("Html", "CSS", "JS")

# myskills = {
#     'Html' : "80%", 
#     'CSS' : "70%", 
#     'JS' : "64%", 
#     'python' : "71%",
#     'PHP' : "43%"
# }

# def show_skills(**skills) :

#     print(type(skills))
#     for skill, value in skills.items() :
#           print(f"{skill} => {value}")
    
# # show_skills(Html ="80%", CSS = "70%", JS = "64%", python = "71%")
# # print(myskills)
# show_skills(**myskills)


# ---------------------------------------------------
# -- Function Packing, unpacking arguments training --
# ---------------------------------------------------


# myTuple = ("html", "CSS", "JS")
# mySkills = {
#         'Python' : "80%",
#         'PHP' : "61%",
#         'Mysql' : "75%",
#         'Data Science' : "68%",
# }
# def show_skills(name, *skills, **skillwithprogress) :

#     print(f" Hello {name} \nskill without progress is: ")

#     for skill in skills :
#         print(f" - {skill}")

#     print(f"skill with progress is: ")

#     for skill_key, skill_value in skillwithprogress.items() :
#         print(f"- {skill_key} => {skill_value}")

# show_skills("Qusay", *myTuple, **mySkills)



# ------------------
# -- Global Scope --
# ------------------


#x = 1  # global scope

# def one() :
#     global x
#     x = 2
#     print (f"print variable from function scope {x}")

# def two() :
#     #x = 4
#     x = 10
#     print (f"print variable from function scope {x}")

# one()
# print(f"print variable from global scope {x}")
# two()
# print(f"print variable from global scope after x function is {x}")


# ------------------------
# -- Function Recursion --
# -- Function Recursion --
# -----------------------------------------------------------------
# -- To unerstand recursion, you need to first understand recursion
# -----------------------------------------------------------------

# test Word = [wwwwoooorrrrrldddd]

# x = "wwwooorrllllddd"
# print(x[1:])

# def cleanWord (word):

#     if len(word) == 1:

#         return word
    
#     print(f"print start function {word}")

#     if word[0] == word[1]:  # WWWoooorrrlllddd
#         print(f"print before condition {word}")

#         return cleanWord(word[1:])
    
#     print(f"print before return {word}")

#     return word[0] + cleanWord(word[1:])
    
#     # Stach [ World ]
# print(cleanWord("WWWoooorrrlllddd"))



# ------------------------
# --  Function => lambda--
# -- Anonymous Function --
# -----------------------------------------------------------------
# [1] It has no name
# [2] You can call it inline without defining it
# [1] You can use it in return data from another function
# [1] Lambda used for simple functions and def handle the large task
# [1] Lambda is One single expression not nlock of code
# [1] Lambda type i function
# -----------------------------------------------------------------


# def say_hello(name, age): return f"hello {name} your age is {age}"

# hello = lambda name, age : f"hello {name} your age is {age}"

# print(say_hello("Ahmed", 28))
# print(hello ("Abdo", 28))

# print(say_hello.__name__) # function name
# print(hello.__name__)     # Anonymous , no name


# print(type(hello))