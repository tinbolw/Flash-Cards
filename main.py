import os

continue1 = ""
question1 = ""
answer1 = ""
continue2 = ""
question2 = ""
answer2 = ""
questionsAmount = 0
questionsCorrect = 0


def askQuestion2():
	global question2
	global answer2
	global questionsAmount
	global questionsCorrect
	print(question2)
	evaluate2 = input("What is the answer?\n")
	if evaluate2 == answer2:
		print("Correct!\n")
		questionsAmount = int(questionsAmount)
		questionsCorrect = int(questionsCorrect)
		questionsCorrect += 1
		questionsAmount = str(questionsAmount)
		questionsCorrect = str(questionsCorrect)
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		askQuestion3()
	elif evaluate2 != answer2:
		print("Incorrect!")
		askQuestion2()


def askQuestion1():
	global question1
	global question2
	global answer1
	global questionsAmount
	global questionsCorrect
	print(question1)
	evaluate1 = input("What is the answer?\n")
	if evaluate1 == answer1:
		print("Correct!\n")
		questionsAmount = int(questionsAmount)
		questionsCorrect = int(questionsCorrect)
		questionsCorrect += 1
		questionsAmount = str(questionsAmount)
		questionsCorrect = str(questionsCorrect)
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		if question2 == "":
			quit()
		askQuestion2()
	elif evaluate1 != answer1:
		print("Incorrect!")
		if question2 == "":
			quit()
		askQuestion2()

def funcContinue2():
	if continue2 == "Y" or continue1 == "y" or continue1 == "yes" or continue1 == "Yes":
		getCard3()
	elif continue1 == "N" or continue1 == "n" or continue1 == "no" or continue1 == "No":
		os.system('cls' if os.name == 'nt' else 'clear')
		askQuestion1()
	else:
		print("Invalid Selection")
		funcContinue2()

def getCard2():
	global question2
	global continue2
	global answer2
	global questionsAmount
	question2 = input("What is the question?\n")
	answer2 = input("What is the answer?\n")
	continue2 = input("Continue? (Y/N)\n")
	questionsAmount += 1
	funcContinue2()

def funcContinue1():
	if continue1 == "Y" or continue1 == "y" or continue1 == "yes" or continue1 == "Yes":
		getCard2()
	elif continue1 == "N" or continue1 == "n" or continue1 == "no" or continue1 == "No":
		os.system('cls' if os.name == 'nt' else 'clear')
		askQuestion1()
	else:
		print("Invalid Selection")
		funcContinue1()


def getCard1():
	global question1
	global continue1
	global answer1
	global questionsAmount
	question1 = input("What is the question?\n")
	answer1 = input("What is the answer?\n")
	continue1 = input("Continue? (Y/N)\n")
	questionsAmount += 1
	funcContinue1()

getCard1()
