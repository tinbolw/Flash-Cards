import os

done = None

questionsCorrect = 0
questionsAmount = 0
question1 = ""
answer1 = ""
question2 = ""
answer2 = ""

def askQuestion2():
	print("wip")

def askQuestion1():
	global question1
	global questionsCorrect
	global questionsAmount
	global answer1
	print(question1)
	answer = input("What is the answer?\n")
	answer = str(answer)
	if answer == answer1:
		print("Correct!")
		questionsCorrect += 1
		questionsCorrect = str(questionsCorrect)
		questionsAmount = str(questionsAmount)
		print("Your score is: " + questionsCorrect + "/" + questionsAmount)
		askQuestion2()
	elif answer != answer1:
		tryagain = input("Incorrect\nDo you want to try again?\n")
		tryagain = str(tryagain)
		if tryagain == "Y" or "y" or "yes" or "Yes":
			askQuestion1()
		elif tryagain == str(N) or "n" or "no" or "No":
			askQuestion2()

def askDone():
	global done
	done = input("Are you done?\n")
	done = str(done)

def getQuestion2():
	global answer2
	global done
	global questionsAmount
	global question2
	question2 = input("What is the question?\n")
	answer2 = input("What is the answer?\n")
	questionsAmount += 1
	askDone()
	if done == "Y" or "y" or "yes" or "Yes":
		print("Ok")
		os.system('cls' if os.name == 'nt' else 'clear')
		askQuestion2()
	elif done == "N" or "n" or "no" or "No":
		done = None
		getQuestion3()

def getQuestion1():
	global answer1
	global done
	global questionsAmount
	global question1
	question1 = input("What is the question?\n")
	answer1 = input("What is the answer?\n")
	questionsAmount += 1
	askDone()
	if done == "Y" or "y" or "yes" or "Yes":
		print("Ok")
		os.system('cls' if os.name == 'nt' else 'clear')
		askQuestion1()
	elif done == "N" or "n" or "no" or "No":
		done = None
		getQuestion2()

getQuestion1()
