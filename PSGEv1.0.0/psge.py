import random 
print("")
print("Welcome to the text & password generator ....")
print("<---------------------------------------------------------------------------------------------------------------------------------------------->")
print("")
print("Hint: ")
# GET CHOSEN FROM USER
print("   If you want to add a text first, type '1'")
print("   If you want to add a text last, type '2'")
print("   If you want to add a text first & last, type '3'")
print("   Get help: Enter '12' or 'help' command")
print("   Exit: use 'exit' command or '13'")
print("")
chose=str(input(":- ")) # get the input

if(chose=="1"):
	xi =  int(input("Enter the range: "))
	ft = str(input("Enter the text to add: "))
	filename = str(input("Enter the file name to save: "))
	for x in range(xi):
		pros = str(ft)+str(x)
		filer=open(filename, "a")
		filer.write("\n"+str(pros))
		filer.close()
		x+=1
	print("<---------------------------------------------------------------------------------------------------------------------------------------------->")
	print("Bye ... Bye .....")
elif(chose=="2"):
	xi =  int(input("Enter the range: "))
	ft = str(input("Enter the text to add: "))
	filename = str(input("Enter the file name to save: "))
	for x in range(xi):
		pros = str(x)+str(ft)
		filer=open(filename, "a")
		filer.write("\n"+str(pros))
		filer.close()
		x+=1
	print("<---------------------------------------------------------------------------------------------------------------------------------------------->")
	print("Bye ... Bye .....")
elif(chose=="3"):
	xi =  int(input("Enter the range: "))
	ft = str(input("Enter the first text to add: "))
	ftlast = str(input("Enter the last text to add: "))
	filename = str(input("Enter the file name to save: "))
	for x in range(xi):
		pros = str(ft)+str(x)+str(ftlast)
		filer=open(filename, "a")
		filer.write("\n"+str(pros))
		filer.close()
		x+=1
	print("<---------------------------------------------------------------------------------------------------------------------------------------------->")
	print("Bye ... Bye .....")
elif(chose=="12" or chose==" 12" or chose=="Help" or chose=="help" or chose=="HELP"):
	print("<------------------------------>")
	print("Thank you for using this toolkit.")
	print("You can easily control this toolkit with following commands.")
	print(" 1. To add a text before 'gen_numbers'. But, you can't add a text after 'gen_numbers'. command:- 1")
	print("   Ex: ")
	print("       text1")
	print("       text2")
	print("       text3")
	print(" 2. To add a text after 'gen_numbers'. But, you can't add a text before 'gen_numbers'. command:- 2")
	print("   Ex: ")
	print("       1text")
	print("       2text")
	print("       3text")
	print(" 3. To add texts before & after gen_numbers'. command:- 3")
	print("   Ex: ")
	print("       test1@gmail.com")
	print("       test2@gmail.com")
	print("       test3@gmail.com")
	print("")
	print("You can enter a number to range question. After it will process 0 - your input")
	print("")
	print("<------------------------------>")
	print("Good luck!")
	print("<------------------------------>")
	print("Hint: ")
	# GET CHOSEN FROM USER
	print("   If you want to add a text first, type '1'")
	print("   If you want to add a text last, type '2'")
	print("   If you want to add a text first & last, type '3'")
	print("   Get help: Enter '12' or 'help' command")
	print("   Exit: use 'exit' command or '13'")
	print("")
	chose=str(input(":- ")) # get the input

	if(chose=="1"):
		xi =  int(input("Enter the range: "))
		ft = str(input("Enter the text to add: "))
		filename = str(input("Enter the file name to save: "))
		for x in range(xi):
			pros = str(ft)+str(x)
			filer=open(filename, "a")
			filer.write("\n"+str(pros))
			filer.close()
			x+=1
		print("<---------------------------------------------------------------------------------------------------------------------------------------------->")
		print("Bye ... Bye .....")
	elif(chose=="2"):
		xi =  int(input("Enter the range: "))
		ft = str(input("Enter the text to add: "))
		filename = str(input("Enter the file name to save: "))
		for x in range(xi):
			pros = str(x)+str(ft)
			filer=open(filename, "a")
			filer.write("\n"+str(pros))
			filer.close()
			x+=1
		print("<---------------------------------------------------------------------------------------------------------------------------------------------->")
		print("Bye ... Bye .....")
	elif(chose=="3"):
		xi =  int(input("Enter the range: "))
		ft = str(input("Enter the first text to add: "))
		ftlast = str(input("Enter the last text to add: "))
		filename = str(input("Enter the file name to save: "))
		for x in range(xi):
			pros = str(ft)+str(x)+str(ftlast)
			filer=open(filename, "a")
			filer.write("\n"+str(pros))
			filer.close()
			x+=1
		print("<---------------------------------------------------------------------------------------------------------------------------------------------->")
		print("Bye ... Bye .....")
	elif(chose=="12" or chose==" 12" or chose=="Help" or chose=="help" or chose=="HELP"):
		print("<------------------------------>")
		print("Thank you for using this toolkit.")
		print("You can easily control this toolkit with following commands.")
		print(" 1. To add a text before 'gen_numbers'. But, you can't add a text after 'gen_numbers'. command:- 1")
		print("   Ex: ")
		print("       text1")
		print("       text2")
		print("       text3")
		print(" 2. To add a text after 'gen_numbers'. But, you can't add a text before 'gen_numbers'. command:- 2")
		print("   Ex: ")
		print("       1text")
		print("       2text")
		print("       3text")
		print(" 3. To add texts before & after gen_numbers'. command:- 3")
		print("   Ex: ")
		print("       test1@gmail.com")
		print("       test2@gmail.com")
		print("       test3@gmail.com")
		print("")
		print("You can enter a number to range question. After it will process 0 - your input")
		print("")
		print("<------------------------------>")
		print("Good luck!")
		print("<------------------------------>")



