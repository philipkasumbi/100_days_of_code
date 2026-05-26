with open("C:/Users/kasum/OneDrive/Desktop/100 days of code/DAY 24  Mail Merge Project/input/name/invited_names.txt") as file:
    names = file.readlines()

with open("C:/Users/kasum/OneDrive/Desktop/100 days of code/DAY 24  Mail Merge Project/input/letters/starting_letter.txt") as letter:
    letter_content = letter.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter_content.replace("[name]",stripped_name)

    with open(f"C:/Users/kasum/OneDrive/Desktop/100 days of code/DAY 24  Mail Merge Project/output/ReadyToSend/{stripped_name}.txt",mode="w") as file:
        file.write(new_letter)
