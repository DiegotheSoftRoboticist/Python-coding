from random import randint
player_wins = 0
computer_wins = 0

while player_wins < 2 and computer_wins < 2:
	print(f"Player Score: {player_wins}     Computer Score: {computer_wins}")
	print("...Rock...")
	print("...Paper...")
	print("...Scissors...")

	player = input("Diego the softroboticist, make a move!!!!:")
	if player == "quit":
		break
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
			player_wins += 1
		elif computer == "Paper":
			print("computer wins!")
			computer_wins += 1
	elif player == "Paper":
		if computer == "Rock":
			print("player wins!")
			player_wins += 1
		elif computer == "Scissors":
			print("computer wins!")
			computer_wins += 1
	elif player == "Scissors":
		if computer == "Paper":
			print("player wins!")
			player_wins += 1
		elif computer == "Rock":
			print("computer wins!")
			computer_wins += 1
	else:
		print("Something went wrong")
if player_wins > computer_wins:
	print(f"FINAL SCORE: Player Score: {player_wins}  Computer Score: {computer_wins}")
	print("Diego WON!")
else:
	print(f"FINAL SCORE: Player Score: {player_wins}  Computer Score: {computer_wins}")
	print("The Computer won! Probably cheating!!")