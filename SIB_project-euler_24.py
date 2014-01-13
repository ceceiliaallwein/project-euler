'''
PROJECT EULER 

24
LEXICOGRAPHIC PERMUTATIONS
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 

If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

'''


from itertools import permutations

def make_list(x,y):
	'''Creates a list from given range.''' 
	output = range(x,y+1)
	return output 

def format(perm):
	'''Converts permutation, i.e. a 
	list of ints, into single int.''' 
	output = int(''.join(str(num) for num in perm))
	return output


def choose_permutation(x,y,n):
	'''Generates n permutations from a list of a
	given range. Returns the n-th permutation.'''  
	# Generates tuple of permutations
	x = [permutations(make_list(x,y),r=None) for perm in range(n)]
	# Converts tuple to list and selects n-th permutation
	x = list(x[n-1])
	x = x[n-1]
	# Formats permutation as int
	x = format(x)
	return x

# Prints the millionth lexocographical permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
print choose_permutation(0,9,1000000)








