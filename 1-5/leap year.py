# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap_year = False
even_div_by_four = False
even_div_by_one_hundred = False
even_div_by_four_hundred = False
mod_four = year % 4
mod_one_hundred = year % 100
mod_four_hundred = year % 400


if mod_four == 0:
    even_div_by_four = True
if mod_one_hundred == 0:
    even_div_by_one_hundred = True
if mod_four_hundred == 0:
    even_div_by_four_hundred = True

# on every year that is evenly divisible by 4
# **except** every year that is evenly divisible by 100
# **unless** the year is also evenly divisible by 400

#2020 True, False, False // it is leap year
#2016 True, False, False // it is a leap year
#2000 True, True, True // it is a leap year
#1989 False, False, False // not a leap year

if even_div_by_four == True and even_div_by_one_hundred == False and even_div_by_four_hundred == False:
    leap_year = True


print(f"even_div_by_four: {even_div_by_four}")
print(f"even_div_by_one_hundred: {even_div_by_one_hundred}")
print(f"even_div_by_four_hundredd: {even_div_by_four_hundred}")
print(f"mod_four: {mod_four}, mod_one_hundred: {mod_one_hundred} mod_four_hundred: {mod_four_hundred}")

if leap_year:
    print('Leap year.')
else:
    print('Not leap year.')

