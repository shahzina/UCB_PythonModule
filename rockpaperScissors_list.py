import random


r = "rock"
p = "paper"
s = "scissors"

game = ["r","p","s"]

user = input("What do you choose?") #variable for user input
gen = random.choice(game) #variable for random generation
print("Computer printed", gen)
if user == gen:
	print ("You've tied!")
elif (user is "r" & gen is "s"):
	print("Sorry, try again.")
elif (user is "r" & gen is "p"):
	print("Whoa! You've won.")
elif (user is "p" & gen is "s"):
	print("Whoa! You've won.")
else:
	print("There's a mistake somewhere.")
