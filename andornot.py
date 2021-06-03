print("how many siblings do you have?")
siblings = input()
siblings = int(siblings)
# siblings =2
if siblings == 0:
	print("you are a like person")
elif (siblings >= 1 and siblings < 3):
	print("Life can be rough")
else:
	print("I feel your pain")
