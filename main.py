
questionsCorrect = 0
questionsAmount = 0
question1 = ""
answer1 = ""
isDone = ""

def askQuestion1():
	global questionsCorrect
	global question1
	global answer1
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


def getQuestion1():
	global questionsAmount
	global question1
	global answer1
	question1 = input("What is the question?\n")
	answer1 = input("What is the answer?\n")
	questionsAmount += 1
	isDone = input("Are you done? (Y/N)\n")
	isDone = str(isDone)
	def checkDone1():
		if isDone == str(Y):
			print("Ok")
			askQuestion1()
		elif isDone == str(N):
			getQuestion2()
		else:
			print("Invalid Selection")
			checkDone1()
	checkDone1()

getQuestion1()
