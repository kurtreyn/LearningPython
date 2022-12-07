############DEBUGGING#####################

# Describe Problem
def my_function():
  """ solved by changing range(1,20) to range(1,21) """
  for i in range(1, 21):
    if i == 20:
      print("You got it")
# my_function()

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# dice_num = 6 # 6 is out of range
dice_num = randint(1, 5)
# print(dice_imgs[dice_num])

# Play Computer
# year = int(input("What's your year of birth? "))
# # if year > 1980 and year < 1994:
# #   print("You are a millenial.")
# # elif year > 1994:
# #   print("You are a Gen Z.")
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#   print(f"You can drive at age {age}.")

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# # word_per_page == int(input("Number of words per page: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"pages: {pages}, words_per_page: {word_per_page}, total_words: {total_words}")
# print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  # b_list.append(new_item)
    b_list.append(new_item) # indent line so it is in the loop
  print(b_list)

# mutate([1,2,3,5,8,13])