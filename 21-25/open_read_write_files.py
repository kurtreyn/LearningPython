# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close() # must manually close the file

# ** READ MODE
# with open("my_file.txt") as file:
# 	contents = file.read()
# 	print(contents)
# 	# same as above except we don't have to remember to manually close the file

# ** WRITE MODE
# with open("my_file.txt", mode='w') as file:
# 	new_content = file.write("Erasing original content of text file and creating new content. Open the file to see.")
# 	print(new_content)


# ** APPEND MODE
# with open("my_file.txt", mode='a') as file:
# 	add_content = file.write("\nAdding new content to the text file. Open the file to see.")
# 	print(add_content)

# # ** CREATE NEW FILE (MUST BE IN WRITE MODE)
# with open("new_file.txt", mode='w') as file:
# 	new_content = file.write("Made a new file.")
# 	print(new_content)

# ** OPEN FILE IN ANOTHER DIRECTORY
with open("./sub_dir/my_other_file.txt") as file:
	contents = file.read()
	print(contents)