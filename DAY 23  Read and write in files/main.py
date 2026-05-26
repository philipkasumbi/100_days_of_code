# reading file and closing
file = open("my_text.txt")
contents = file.read()
print(contents)
file.close()

# reading file
with open("my_text.txt") as file:
    contents = file.read()
    print(contents)


# writing to a file
with open("my_text.txt",mode="w") as file:
    file.write("New text")

# append to a file
with open("my_text.txt",mode="a") as file:
    file.write("\nNew text")

# writing to a new file
with open("new_text.txt",mode="w") as file:
    file.write("This is a new text file")