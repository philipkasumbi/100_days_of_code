
total_height = 0
height=[123,128,130,150,146,112,107,160]

for h in height:
    total_height +=h
    average_height = total_height/len(height)
print(round(average_height))