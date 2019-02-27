'''
Create a simple Python command line application. 
Upon running, the application should:


Print "Hello User!"
Then ask: "What is your name? "
Then respond: "Hello <user's name>"
Then ask: "What is your age? "
Then respond: "Awww... you're just a baby!" or "Ah... A well 
traveled soul are ye." depending on the user's age.

'''

print('Hello user!')

name = input('What is your name?')
print("Hello" + name + "!")

age = input(int(("How old are you?"))

if (int(age) < 14):
	print("Awww... you're just a baby!")
else:
	print("Ah... a well traveled soul are ye.")