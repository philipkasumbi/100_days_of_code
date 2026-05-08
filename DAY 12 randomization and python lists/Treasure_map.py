row1 = ["🔘","🔘","🔘"]
row2 = ["🔘","🔘","🔘"]
row3 = ["🔘","🔘","🔘"]

map = [row1,row2,row3]  

print(f"{row1}\n{row2}\n{row3}\n")

position = input("Where do you want to put the treaure? numbers should be between 1 and 3 e.g 23 \n")

row = int(position[0])
col = int(position[1])

row -= 1
col -= 1    

selected_col = map[col]
selected_col[row] = "X"

print(f"{row1}\n{row2}\n{row3}\n")