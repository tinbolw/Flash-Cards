
continue1 = ""
question1 = ""
answer1 = ""
questionsAmount = 0
questionsCorrect = 0

def getCard2():
	question2 = input("What is the question?\n")
	answer2 = input("What is the answer?\n")
	continue2 = input("Continue? (Y/N)\n")

def askQuestion2():
	print("WIP")


def askQuestion1():
	global question1
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
		askQuestion2()
	elif evaluate1 != answer1:
		def funcTryAgain1():
			tryAgain1 = ("Incorrect\nWould you like to try again? (Y/N)\n")
			if tryAgain1 == "Y" or tryAgain1 == "y" or tryAgain1 == "yes" or tryAgain1 == "Yes":
				askQuestion1()
			elif tryAgain1 == "N" or tryAgain1 == "n" or tryAgain1 == "no" or tryAgain1 == "No":
				print("Ok, skipping to question 2\n")
				askQuestion2()
			else:
				print("Invalid Selection")
				funcTryAgain1()


def funcContinue1():
	if continue1 == "Y" or continue1 == "y" or continue1 == "yes" or continue1 == "Yes":
		getCard2()
	elif continue1 == "N" or continue1 == "n" or continue1 == "no" or continue1 == "No":
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
