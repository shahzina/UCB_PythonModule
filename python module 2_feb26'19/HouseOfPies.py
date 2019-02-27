
pie_list = ["Pecan","Apple Crisp","Bean","Banoffee","Black Bun","Blueberry","Buko","Burek","Tamale","Steak"]


purchased_pies = []

order_more_pies = "y"

# variable = some value
# do stuff
print("Welcome to the house of pies! Here are our pies: ")

#while variable == some value
while order_more_pies == "y":
	# do more stuff
	print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, "+
		" (5) Black Bun, (6) Blueberry , (7) Buko , " +
		" (8) Burek , (9) Tamale ,(10) Steak ")
# give user opportunity to change value
	pie_choice = input("Which pie would you like?")
	purchased_pies.append(pie_choice)

	print("Great! We'll have that "+ pie_list[int(pie_choice)-1] + " right out for you.")
	
	order_more_pies = input("Would you like to make another purchase: (y)es or (n)o?")

print("You've purchased a total of " + str(len(purchased_pies)) + " pies!")
