
done = None

questionsCorrect = 0
questionsAmount = 0

def askQuestion1():
	global questionsCorrect
	print(question1)
	answer = input("What is the answer?\n")
	answer = str(answer)
	if answer == answer1:
		print("Correct!")
		questionsCorrect += 1
		askQuestion2()
	elif answer != answer1:
		tryagain = input("Incorrect\n Do you want to try again?\n")
		tryagain = str(tryagain)
		if tryagain == "Y" or "y" or "yes" or "Yes":
			askQuestion1()
		elif tryagain == "N" or "n" or "no" or "No":
			askQuestion2

def askDone():
	global done
	done = input("Are you done?\n")
	done = str(done)

def getQuestion1():
	global done
	question1 = input("What is the question?\n")
	answer1 = input("What is the answer?\n")
	questionsAmount += 1
	askDone()
	if done == "Y" or "y" or "yes" or "Yes":
		print("Ok")
		askQuestion1()
	elif done == "N" or "n" or "no" or "No":
		getQuestion2()

getQuestion1()