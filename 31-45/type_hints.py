# Type Hints

def is_adult(age: int) -> bool:
	if age >= 18:
		adult = True
	else:
		adult = False
	return adult


print(is_adult(18))