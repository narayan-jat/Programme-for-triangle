#Given 5 numbers, out one number appears twice and all other numbers are unique.
#Find the number which appears twice. → why is this relevant, what if someone manages to duplicate of which or orderId

#creating list of numbers from users 
numbers = [float(input('Enter the first number: ')), float(input('Enter the first number: ')), float(input('Enter the first number: ')),float(input('Enter the first number: ')), float(input('Enter the first number: '))]

# Function to find the number which is twice one
def find_twice_one(lst):
	'''
	Returns: The number which is appears twice in given five numbers. 
	Float and Integer vlues will be considered SAME i.e 6.0 equal to 6
	numbers with diffrent sign will be considered DIFFERENT 

	parameters lst : This one is list containing all five numbers
	precondition : This must be list type

	>>> find_twice_one([5, 2, 6.4, 8, 6])
	'No velue appeared twice'
	>>> find_twice_one([5, 2, 6.0, 6, 6])
	6
	>>> find_twice_one([5, 2, 6.0, -6, 6])
	'No vlue appeared twice'
	'''
	lst.sort()
	#comparing consecutive elements of list after sorting 
	for x in range(len(lst) - 2) :
		if lst[x] == lst[x+1] :
			return lst[x]
	return 'No value appeared twice'

print(find_twice_one(numbers))

# This is relevant in the conmtext that when a person is managing duplicate orderid then this function will 
#be useful to find that orderid is duplicate
# I am not getting this question (→ why is this relevant, what if someone manages to duplicate of which or orderId)
#yet i tried to answere upto level i understood