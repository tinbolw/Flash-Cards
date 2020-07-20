import os

continue1 = ""
question1 = ""
answer1 = ""
continue2 = ""
question2 = ""
answer2 = ""
questionsAmount = 0
questionsCorrect = 0

def askQuestion5():
	global question5
	global answer5
	global questionsAmount
	global questionsCorrect
	print(question5)
	evaluate5 = input("What is the answer?\n")
	if evaluate5 == answer5:
		print("Correct!\n")
		questionsAmount = int(questionsAmount)
		questionsCorrect = int(questionsCorrect)
		questionsCorrect += 1
		questionsAmount = str(questionsAmount)
		questionsCorrect = str(questionsCorrect)
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		input("Press enter to quit")
	elif evaluate5 != answer5:
		print("Incorrect!")
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		input("Press enter to quit")

def askQuestion4():
	global question4
	global answer4
	global questionsAmount
	global questionsCorrect
	print(question4)
	evaluate4 = input("What is the answer?\n")
	if evaluate4 == answer4:
		print("Correct!\n")
		questionsAmount = int(questionsAmount)
		questionsCorrect = int(questionsCorrect)
		questionsCorrect += 1
		questionsAmount = str(questionsAmount)
		questionsCorrect = str(questionsCorrect)
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		if question5 == "":
			input("Press enter to quit")
		askQuestion5()
	elif evaluate4 != answer4:
		print("Incorrect!")
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		if question5 == "":
			input("Press enter to quit")
		askQuestion5()

def askQuestion3():
	global question3
	global answer3
	global questionsAmount
	global questionsCorrect
	print(question3)
	evaluate3 = input("What is the answer?\n")
	if evaluate3 == answer3:
		print("Correct!\n")
		questionsAmount = int(questionsAmount)
		questionsCorrect = int(questionsCorrect)
		questionsCorrect += 1
		questionsAmount = str(questionsAmount)
		questionsCorrect = str(questionsCorrect)
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		if question4 == "":
			input("Press enter to quit")
		askQuestion4()
	elif evaluate3 != answer3:
		print("Incorrect!")
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		if question4 == "":
			input("Press enter to quit")
		askQuestion4()

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
		if question3 == "":
			input("Press enter to quit")
		askQuestion3()
	elif evaluate2 != answer2:
		print("Incorrect!")
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		if question3 == "":
			input("Press enter to quit")
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
			input("Press enter to quit")
		askQuestion2()
	elif evaluate1 != answer1:
		print("Incorrect!")
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		if question2 == "":
			quit()
		askQuestion2()

def funcContinue5():
	if continue5 == "Y" or continue5 == "y" or continue5 == "yes" or continue5 == "Yes":
		getCard5()
	elif continue5 == "N" or continue5 == "n" or continue5 == "no" or continue5 == "No":
   		os.system('cls' if os.name == 'nt' else 'clear')
   		askQuestion1()
 	else:
   		print("Invalid Selection")
   		funcContinue5()

def getCard5():
	global question5
	global continue5
	global answer5
	global questionsAmount
	question5 = input("What is the question?\n")
	answer5 = input("What is the answer?\n")
	continue5 = input("Continue? (Y/N)\n")
	questionsAmount += 1
	funcContinue5()

def funcContinue4():
	if continue4 == "Y" or continue4 == "y" or continue4 == "yes" or continue4 == "Yes":
		getCard5()
	elif continue4 == "N" or continue4 == "n" or continue4 == "no" or continue4 == "No":
   		os.system('cls' if os.name == 'nt' else 'clear')
   		askQuestion1()
 	else:
   		print("Invalid Selection")
   		funcContinue4()

def getCard4():
	global question4
	global continue4
	global answer4
	global questionsAmount
	question4 = input("What is the question?\n")
	answer4 = input("What is the answer?\n")
	continue4 = input("Continue? (Y/N)\n")
	questionsAmount += 1
	funcContinue4()


def funcContinue3():
	if continue3 == "Y" or continue3 == "y" or continue3 == "yes" or continue3 == "Yes":
		getCard4()
	elif continue3 == "N" or continue3 == "n" or continue3 == "no" or continue3 == "No":
		os.system('cls' if os.name == 'nt' else 'clear')
		askQuestion1()
	else:
		print("Invalid Selection")
		funcContinue3()

def getCard3():
	global question3
	global continue3
	global answer3
	global questionsAmount
	question3 = input("What is the question?\n")
	answer3 = input("What is the answer?\n")
	continue3 = input("Continue? (Y/N)\n")
	questionsAmount += 1
	funcContinue3()


def funcContinue2():
	if continue2 == "Y" or continue2 == "y" or continue2 == "yes" or continue2 == "Yes":
		getCard3()
	elif continue2 == "N" or continue2 == "n" or continue2 == "no" or continue2 == "No":
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
