print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make a move!!!!   ")
print("No cheating, cheater!\n\n\n" * 20)
player2 = input("Player 2, make a move!!!!   ")

#Optimized code
if player1 == player2:
	print("It is a TIE!!")
elif player1 == "Rock":
	if player2 == "Scissors":
		print("player1 wins!")
	elif player2 == "Paper":
		print("player2 wins!")
elif player1 == "Paper":
	if player2 == "Rock":
		print("player1 wins!")
	elif player2 == "Scissors":
		print("player2 wins!")
elif player1 == "Scissors":
	if player2 == "Paper":
		print("player1 wins!")
	elif player2 == "Rock":
		print("player2 wins!")
else:
	print("Something went wrong")