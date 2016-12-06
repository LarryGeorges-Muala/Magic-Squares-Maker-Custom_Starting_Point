#App Name: Magic Square Maker with custom starting points - Python
#Python Version 3.5
#Developper: Larry Georges Muala


#odd number input checking function
def oddCheck(n):
	n = int( input("\nPlease Enter an odd number: ") )
	
	if n % 2 != 0:
		magicSquare(n)
	else:
		oddCheck(n)

		
#magic square drawing function		
def magicSquare(n):	
	#creating the magic square layout and populating it with zeros
	magic_list = [[ 0 for column_s in range(n) ] for row_s in range(n)]


	#loops to assign magic square values to each entry in magic_list
	#using formula:
	# for Ith row and Jth column
	# value = { n*[(I + J - 1 + (n//2)) % n)] } + { [(I + 2*J - 2) % n] + 1 }

	for row_s in range(n):
		for column_s in range(n):
		
			row_value = row_s + 1
			column_value = column_s + 1

			value = ( n * ((row_value + column_value - 1 + (n//2)) % n) ) + ( ((row_value + 2 * column_value - 2) % n) + 1 )
			
			magic_list[row_s][column_s] = value
			
	magic_list_reverse = []
	magic_list_reverse = magic_list[::-1]
	magic_list_temp = []
	magic_list_temp2 = []
	magic_list_temp3 = []
	magic_list_temp4 = []
	
	def top_Middle():
		print("")
		#formatting magic_list by splitting elements and joining by 4 digits space
		for m in range(n):
			print(' '.join( '{:4d}'.format(x) for x in magic_list[m] ))

	def bottom_Middle():
		print("")
		#formatting magic_list by splitting elements and joining by 4 digits space
		for m in range(n):
			print(' '.join( '{:4d}'.format(x) for x in magic_list_reverse[m] ))
			
	def left_Middle():
		print("")
		
		#looping through magic_list to retrieve every single element of the list
		for y in range(n):
			for x in magic_list:
				magic_list_temp.append(x[y])
		
		#grouping elements to create a new positioning
		magic_list_temp2 = [magic_list_temp[x:x+n] for x in range(0, len(magic_list_temp), n)]
		
		#formatting magic_list by splitting elements and joining by 4 digits space
		for m in range(n):
			print(' '.join( '{:4d}'.format(x) for x in magic_list_temp2[m] ))
	
	def right_Middle():
		print("")
		
		#looping through magic_list to retrieve every single element of the list
		for y in range(n):
			for x in magic_list_reverse:
				magic_list_temp3.append(x[y])
		
		#grouping elements to create a new positioning
		magic_list_temp4 = [magic_list_temp3[x:x+n] for x in range(0, len(magic_list_temp3), n)]
		
		#formatting magic_list by splitting elements and joining by 4 digits space
		for m in range(n):
			print(' '.join( '{:4d}'.format(x) for x in magic_list_temp4[m] ))
	
	#starting points selector
	print("\n *Starting Points* \n\n1.Top Middle \n2.Bottom Middle \n3.Left Middle \n4.Right Middle \n")
	
	starting_point = int( input("\nChoose your Starting Point: ") )
	
	if starting_point == 1:
		top_Middle()
		
	elif starting_point == 2:
		bottom_Middle()
		
	elif starting_point == 3:
		left_Middle()
		
	elif starting_point == 4:
		right_Middle()
		
	else:
		print("\n~Incorrect Entry~ \nDisplaying All starting Points \n")
		
		print("\nTop Middle")
		top_Middle()
		
		print("\nBottom Middle")
		bottom_Middle()
		
		print("\nLeft Middle")
		left_Middle()
		
		print("\nRight Middle")
		right_Middle()
		
	
#ask user for size of magic square, making sure it is a number
n = int( input("\nEnter the size of the magic square: ") )

#check that the input is odd with the oddCheck function
if n % 2 != 0:
	magicSquare(n)
	
else:
	oddCheck(n)