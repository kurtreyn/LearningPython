# from turtle import Turtle, Screen
# from prettytable import PrettyTable
# ** Attributes are variables in a class
# ** Methods are functions in a class
# timmy_turtle = Turtle()

# print(timmy_turtle)

# timmy_turtle.shape("turtle")
# timmy_turtle.color("coral")
# timmy_turtle.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

# table = PrettyTable()
#
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"

# print(table)

# ** Creating a Class **
class User:
	def __init__(self, user_id, username):
		self.id = user_id
		self.username = username
		self.followers = 0
		self.following = 0

	def follow(self, user):
		user.followers += 1
		self.following += 1



user_1 = User("001", "Kurt")
user_2 = User("002", "Scarlett")

user_1.follow(user_2)

print(f"user_1 followers: {user_1.followers}")
print(f"user_1 following: {user_1.following}")
print(f"user_2 followers: {user_2.followers}")
print(f"user_2 following: {user_2.following}")
