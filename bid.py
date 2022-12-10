logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
bid = {}
over = False

def highest(bid):
    highest = 0
    winner = ""
    for i in bid:
        bid_amt = bid[i]
        if bid_amt > highest:
            highest = bid_amt
            winner = i
    print(f"The Winner is {winner} with a bid of {highest}")

while not over:
    key = input("What is your name? ")
    price = int(input("What is your bid price? "))
    bid[key] = price
    result = input("Are there any other bidders? Type yes or no").lower()
    if(result == "no"):
        over = True
        highest(bid)
        
