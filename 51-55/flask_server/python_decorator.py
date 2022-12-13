import time


def delay_decorator(function):
	def wrapper_function():
		time.sleep(2)
		# Do something before the function
		function()
		# Do something after the function
	return wrapper_function


@delay_decorator
def say_hello():
	time.sleep((2))
	print("Hello")


@delay_decorator
def say_bye():
	print("Bye")


def say_greeting():
	print("How are you?")


say_bye()