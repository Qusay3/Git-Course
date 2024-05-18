
"""friends = ["Mustafa", "Moe", "Sami"]
print(friends)
print(friends[0])
friends.append("Nikki")
friends.reverse()
friends[1] = "Yassin"
print(friends)"""

lucky_numbers = [1,7,3,6,9,5,-3,14,20,0]
friends = ["Mustafa", "Moe", "Sami" , "Ibra", "Joe", "Nizar", "Geety", "Paul", "Khaled", "Miz"]
print(len(lucky_numbers))
print(len(friends))
print(lucky_numbers[4:8])
print(friends[8:])
friends.extend(lucky_numbers)
friends.append("Sona")
friends.insert(1, "omer")
friends.remove(3)
friends.pop()
friends.index("Nizar")
print(friends)
