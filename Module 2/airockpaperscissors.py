
from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")

player = input("Diego the softroboticist, make a move!!!!:   ")
rand_num = randint(0,2)

if rand_num == 0:
	computer = "Rock"
elif rand_num == 1:
	computer = "Paper"
else:
	computer = "Scissors"
print(f"Computer plays {computer}" )




#Optimized code
if player == computer:
	print("It is a TIE!!")
elif player == "Rock":
	if computer == "Scissors":
		print("player wins!")
	elif computer == "Paper":
		print("computer wins!")
elif player == "Paper":
	if computer == "Rock":
		print("player wins!")
	elif computer == "Scissors":
		print("computer wins!")
elif player == "Scissors":
	if computer == "Paper":
		print("player wins!")
	elif computer == "Rock":
		print("computer wins!")
else:
	print("Something went wrong")
