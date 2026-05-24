def divide_numbers(a,b):
	try : 
		return a/b
	except :
		return "Cannot divide by zero"
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))