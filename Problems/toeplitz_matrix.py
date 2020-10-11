# input is a square matrix
def is_toeplitz(mat):

	diag = mat[0][0]
	for i in range(len(mat)):
		if mat[i][i] != diag:
			return False
	return True



m = [[4, 4, 5, 6],
	[2, 4, 4, 5],
	[1, 2, 4, 4],
	[0, 2, 4, 4]]

print(is_toeplitz(m))