game_dic = {1:"Rock", 2:"Paper", 3:"Scissors"}
win_combos = {(1,3): "P1 wins", (2,1): "P1 wins", (3,2): "P1 wins", 
				(3,1): "P2 wins", (1,2): "P2 wins", (2,3): "P2 wins"}
import random

class TheGame:
	def __init__(self, Player1: int, Player2: int):
		self.Player1 = Player1
		self.Player2 = Player2

	def CheckTheWinner(self):
		print("P1:" + game_dic[self.Player1] + ", P2:" + game_dic[self.Player2])
		print ('Draw' if self.Player1 == self.Player2
		 	else win_combos[tuple(map(int, [self.Player1, self.Player2]))])

TheGame(random.randrange(1,4),
 			random.randrange(1,4)).CheckTheWinner()