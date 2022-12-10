row1 = ["🔥","🔥","🔥"]
row2 = ["🔥","🔥","🔥"]
row3 = ["🔥","🔥","🔥"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure?")
pos = str(position)
a=int(pos[0])-1
b=int(pos[1])-1
map[b][a] = "x"
print(f"{row1}\n{row2}\n{row3}")
