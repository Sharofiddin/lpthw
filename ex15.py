from sys import argv

# read filename from cmd line args
script, filename = argv

# open file
txt = open(filename)

# print file name and content
print(f"Here's your file{filename}")
print(txt.read())
txt.close()
# read file again
print("Type the filename again:")
file_again = input("> ")

# read file again which it's name has been got from input prompt
txt_again = open(file_again)

# display again read file content
print(txt_again.read())
txt_again.close()
