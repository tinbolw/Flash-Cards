
continue1 = ""

def getCard2():
	question2 = input("What is the question?\n")
	answer2 = input("What is the answer?\n")
	continue2 = input("Continue? (Y/N)\n")

def askQuestion2():
	print("WIP")


def askQuestion1():
	print(question1)
	evaluate1 = input("What is the answer?\n")
	if evaluate1 == answer1:
		print("Correct!\n")
	elif evaluate1 != answer1:
		def funcTryAgain1():
			tryAgain1 = ("Incorrect\nWould you like to try again? (Y/N)\n")
			if tryAgain1 == str("Y"):
				askQuestion1()
			elif tryAgain1 == str("N"):
				print("Ok, skipping to question 2\n")
				askQuestion2()
			else:
				print("Invalid Selection")
				funcTryAgain1()


def funcContinue1():
	if continue1 == str("Y"):
		getCard2()
	elif continue1 == str == str("N"):
		askQuestion1()
	else:
		print("Invalid Selection")
		funcContinue1()


def getCard1():
	global continue1
	question1 = input("What is the question?\n")
	answer1 = input("What is the answer?\n")
	continue1 = input("Continue? (Y/N)\n")
	funcContinue1()

getCard1()
