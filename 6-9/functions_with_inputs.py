# Functions with inputs

# Simple function
def greet():
	print('Hello')
	print('How are you?')
	print('Good to see you')


# greet()

def greet_with_input(name):
	print(f"Hi {name}")


# greet_with_input('Kurt')

# Functions with more than one input
# example of positional function
def greet_with(name, location):
	print(f"Hi {name}. Are you new to {location}?")

# greet_with('Bob', 'Louisville')

# Example of keyword argument function
greet_with(location='Louisville', name='George')



