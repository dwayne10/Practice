def NQueens(n):

	res = []
	perm - [None]*n
	

	def solve():
		for i in range(n):
				for j in range(n):
					perm[i] = j
					if isValid(perm, n, i):
						res.append(perm)




def isValid():

	diff 

	for i in range(len(perm)):
		if diff == 0 or abs(perm[i] - row) <= 1:
			return False



	return True 