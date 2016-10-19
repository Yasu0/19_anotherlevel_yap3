"""
============
R vs S vs P
============

***************
Game Info
***************
#. Made In Korea

#. Made by Kwon Jae Hoon

#. Very good 


How to win
============
=======  ========  =======
Player   Computer  Result
=======  ========  =======
Rock     Scissor    P win
Rock     Rock       Draw
Rock     Paper      P lose
Scissor  Scissor    Draw
Scissor  Rock       P lose
Scissor  Paper      P win
Paper    Scissor    P lose
Paper    Rock       P win
Paper    Paper      Draw
=======  ========  =======
 
"""









import random




def RSP():

	computer_list = ['Rock','Scissor','Paper']
	random.shuffle(computer_list)
	finish = 'O'
	while(finish != 'X') :
		
		random.shuffle(computer_list)
		a = input(" Choose one of Rock(= R), Scissor(= S),Paper(= P) : ")
		#while (a!='R' or a!='S' or a!='P'):
		#	a = input("input rightly… Choose one of Rock(= R), Scissor(= S),Paper(= P) : ")
		if a=='R':
			a = 'Rock'
		elif a=='S':
			a = 'Scissor'
		elif a=='P':
			a = 'Paper'

		print("——————————————————\n\n\n\n\n\n")
		# 무승부
		if a == computer_list[0] :

			print("   YOU   :",a,"\n\nComputer :",computer_list[0],"\n\n\n———DRAW———")
			#a = input("\n Choose one of Rock(= R), Scissor(= S),Paper(= P) : ")
			#while (a!=R or a!=S or a!=P):
			#	a = input("input rightly… Choose one of Rock(= R), Scissor(= S),Paper(= P) : ")

		#가위 승패
		elif a=='Scissor' and computer_list[0]=='Paper' :
			print("   You   :",a,"\n\nCoumputer :",computer_list[0],"\n\n\n————YOU WIN————")
		elif a=='Scissor' and computer_list[0]=='Rock' :
			print("   You   :",a,"\n\nCoumputer :",computer_list[0],"\n\n\n————YOU Lose————")

		#주먹 승패
		elif a=='Rock' and computer_list[0]=='Scissor' :
			print("   You   :",a,"\n\nCoumputer :",computer_list[0],"\n\n\n————YOU WIN————")
		elif a=='Rock' and computer_list[0]=='Paper' :
			print("   You   :",a,"\n\nCoumputer :",computer_list[0],"\n\n\n————YOU Lose————")

		#보자기 승패
		elif a=='Paper' and computer_list[0]=='Rock' :
			print("   You   :",a,"\n\nCoumputer :",computer_list[0],"\n\n\n————YOU WIN————")
		elif a=='Paper' and computer_list[0]=='Scissor' :
			print("   You   :",a,"\n\nCoumputer :",computer_list[0],"\n\n\n————YOU Lose————")
		print("\n\n\n\n\n——————————————————\n\n\n\n")
		finish = input("Do You Want to Play More? (O/X) : ")




RSP()