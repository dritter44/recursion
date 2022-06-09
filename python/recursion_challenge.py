def factorial(x):
	#recursive algo to find factorial of a number
	if x < 2:
		return 1
	if x > 1:
		return factorial(x-1)*x

def palindrome(string):
	working_arr = list(string)
	#print(working_arr,len(working_arr)) to verify that worrking array was only 1 element long

	#base case: 
	if len(working_arr)  < 2:
		return True

	if len(working_arr) >= 2:
		# print(working_arr[0],working_arr[len(working_arr)-1] ) #to view the working array after a recursive call
		if working_arr[0] == working_arr[len(working_arr)-1]:
			working_arr.pop(0)
			working_arr.pop()
			string = ''.join(working_arr)
			return palindrome(string)
		else:
			return False

def bottles(num):
	pass

def roman_num(num):
	pass


#print(factorial(4))
print(palindrome('madam'))