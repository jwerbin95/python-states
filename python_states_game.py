import random
from states import *

total_correct = 0
start_again = True

def checkKey(key, i):
	if key in states[i].keys():
		return True
	else:
		return False

def sortStates(val):
	return val["incorrect"]

random.shuffle(states)

while start_again:
	print("Welcome to the state and capital quiz. Let's learn our states and capitals!")

	for i in range(len(states)):
		print(f"*********************Question {i+1}********************")
		answer=input(f'What is the capital of {states[i]["name"]}? (Type "Hint" for a hint.)')
		if answer.upper() == "HINT":
			print(states[i]["capital"][:3:])
			answer=input(f'What is the capital of {states[i]["name"]}?')
		if not checkKey("correct", i) and not checkKey("incorrect", i):
			states[i]["correct"] = 0
			states[i]["incorrect"] = 0
		if(answer.upper() != states[i]["capital"].upper()):
			print("Incorrect")
			states[i]["incorrect"]+=1
		else:
			print("Correct")
			total_correct+=1
			states[i]["correct"]+=1
		print(f"You have answered this question {states[i]['correct']} times correctly and {states[i]['incorrect']} times incorrectly and {states[i]['correct']+states[i]['incorrect']} times in total.")
		print(f"Correct answers out of 50:")
		print(total_correct)
		print("***************************************************")
	check=input(f"Play again (Y/N)?")
	start_again=(True if check.upper()=="Y" else False)
	states.sort(key=sortStates, reverse=True)







