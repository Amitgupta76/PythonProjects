import random
names_string = input("Give me names")
names=names_string.split(", ")

random_integer = random.randint(0,len(names)-1)
print(names[random_integer])

