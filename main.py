import program

while True:
	text = input('Project > ')
	result, error = basic.run('<stdin>', text)

	if error: print(error.as_string())
	elif result: print(result)