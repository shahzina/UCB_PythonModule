# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

for i in candyList:
	print(candyList.index(i))
	print (i)
	#print("[" + {candyList.index(i)} + "]" + candy)

# The amount of candy the user will be allowed to choose
allowance = 5
k=0
while k <= allowance:
	print("Would you like another candy?")
k+=1	

# The list used to store all of the candies selected inside of
candyCart = []

user_choice = input(int("What would you like to have?"))

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)

