logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

import random
from data import data
score = 0
game = True

    
def account(details):
    name = details["name"]
    description = details["description"]
    country = details["country"]
    return f"{name}, a {description}, from {country}"

def compare(choose, player_1, player_2):
    
    no1 = player_1["follower_count"]
    no2 = player_2["follower_count"]
    if choose == "a":
        if no1 > no2:
            return 1
        else:
            return 0
    elif choose == "b":
        if no2 > no1:
            return 1
        else :
            return 0


player_1 = random.choice(data)
player_2 = random.choice(data)

while game:
    print(logo)
    player_1 = player_2
    player_2 = random.choice(data)
    while(player_1 == player_2):
        player_2 = random.choice(data)
    print(f"Compare A: {account(player_1)}")
    print(vs)
    print(f"Against B: {account(player_2)}")
    choose = input("Who has more followers? Type 'A' or 'B': ").lower()
    score += compare(choose, player_1, player_2)
    if(compare(choose, player_1, player_2) == 1):
        print(f"You're right! Current score: {score}.")
    else:
        game = False
        print(f"Sorry, that's wrong. Final score: {score}")














    