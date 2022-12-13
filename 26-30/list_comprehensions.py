# List Comprehension: new_list = [new_item for item in list]

numbers = [1, 2, 3]
new_number_list = [num + 1 for num in numbers]
# print(new_number_list)


name = "Kurt"
letter_list = [letter for letter in name]
# print(letter_list)

range_list = [num * 2 for num in range(1, 5)]
# print(range_list)

# Conditional List Comprehension: new_list = [new_item for item in list if test]

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if(len(name) < 5)]
# print(short_names)

long_names = [name.upper() for name in names if (len(name) > 5)]
# print(long_names)