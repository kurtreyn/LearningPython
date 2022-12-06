# Functions with outputs:

def format_name(f_name, l_name):
	formatted_f_name = f_name.title()
	formatted_l_name = l_name.title()
	return f"{formatted_f_name} {formatted_l_name}"

full_name = format_name("kurt", "reynolds")
# print(full_name)

def format_name_two(f_name, l_name):
	if f_name == "" or l_name == "":
		return "You didn't provide any inputs"
	formatted_f_name = f_name.title()
	formatted_l_name = l_name.title()
	return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name_two(input("What is your first name? "), input("What is your last name? ")))