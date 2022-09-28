# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
final_cost = 0

if size == 'S':
    final_cost = 15
if size == 'M':
    final_cost = 20
if size == "L":
    final_cost = 25
if add_pepperoni == 'Y' and size == 'S':
    final_cost += 2
if add_pepperoni == 'Y' and size == 'M' or add_pepperoni == 'Y' and size == 'L':
    final_cost += 3
if extra_cheese == 'Y':
    final_cost += 1

print(f"Your final bill is: ${final_cost}.")
