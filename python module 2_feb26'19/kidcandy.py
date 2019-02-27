#charles solution

candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]


for candy in candyList:
	print("[" + {candyList.index(i)} + "]" + candy)


allowance = 5 #given


#for user choice
candyCart =[]

for i in range(allowance):
	candy_index = input("Which candy would you like to bring home?")
	candyCart.append(candyList[int(candy_index)])


for chosen_candy in candyCart:
	print(chosen_candy)