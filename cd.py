#http://quantstart.com/articles/Cholesky-Decomposition-in-Python-and-NumPy

from math import sqrt
from pprint import pprint

def cholesky(A):
	"""
	Performs a Cholesky decomposition of A, which must be a symmetric 
	and positive definity matrix. The function returns the lower variant triangular matrix, L.
	"""

	n = len(A)

	# Create zero matrix for L

	L = [[0.0] * n for i in xrange(n)]

	# Perform the Cholesky decomposition
	for i in xrange(n):
		for k in xrange(i+1):
			tmp_sum = sum(L[i][j] * L[k][j] for j in xrange(k))

			if (i == k): # Diagonal elements
				# LaTeX: L_{kk} = \sqrt{ a_[kk} - \sum^{k-1}_{j=1} l^2_{kl}}
				L[i][k] = sqrt(A[i][i] - tmp_sum)
			else:
				# LaTeX: l_{ik} = \frac{1}{l_{kk}} \left( a_{ik} - \sum^{k-1}
				L[i][k] = (1.0 / L[k][k] * (A[i][k] - tmp_sum))
	return L

if __name__ == "__main__":
	A = [[6, 3, 4, 8], [3, 6, 5, 1], [4, 5, 10, 7], [8, 1, 7, 25]]
	L = cholesky(A)
	print "A:"
	pprint(A)

	print "L:"
	pprint(L)

	
