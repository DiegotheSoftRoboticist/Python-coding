print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make a move!!!!   ")
player2 = input("Player 2, make a move!!!!   ")

if player1 =="Rock" and player2 == "Scissors":
	print("player1 wins!")
elif player1 =="Paper" and player2 == "Rocks":
	print("player1 wins!")
elif player1 =="Scissors" and player2 == "Paper":
	print("player1 wins!")

elif player2 =="Rock" and player1 == "Scissors":
	print("player2 wins!")
elif player2 =="Rock" and player1 == "Scissors":
	print("player2 wins!")
elif player2 =="Rock" and player1 == "Scissors":
	print("player2 wins!")

elif player1 == player2:
	print("It is a TIEEE!!")

else:
	print("Something went wrong")
