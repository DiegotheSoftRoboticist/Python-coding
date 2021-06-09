
# for num in range(1,21):
# 	if num == 13 or num == 4:
# 		print(f"{num} is an unlucky number")
# 	elif num % 2 == 0:
# 		 print(f"{num} is an even number")
# 	else:
# 		print(f"{num} is an odd number")

for num in range(1,21):
	if num == 13 or num == 4:
		state = "unlucky"
	elif num % 2 == 0:
		 state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")