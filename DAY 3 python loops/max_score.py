students_score = [31,42,33,56,70,89,97,45,67]

max_score = students_score[0]

for score in students_score:
    if score > max_score:
        max_score = score

print(f"The max score is {max_score}")