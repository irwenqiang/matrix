#http://quantstart.com/articles/QR-Decomposition-with-Python-and-NumPy
from math import sqrt
from pprint import pprint

def mult_matrix(M, N):
	"""Multiply square matrices of same dimension M and N"""
	tuple_N = zip(*N)
	return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def trans_matrix(M):
	n = len(M)
	return [[M[i][j] for i in range(n)] for j in range(n)]


def norm(x):
	return sqrt(sum(x_i ** 2 for x_i in x))

def Q_i(Q_min, i, j, k):
	"""Construct the Q_t matrix by left-top padding the matrix 
	Q with elements from the identity matrix."""
	if i < k or j < k:
		return float(i == j)
	else:
		return Q_min[i-k][j-k]
	
def householder(A):
	"""Performs a Householder Reflections based QR Decomposition of the 
	matrix A. The function returns Q, an orthogonal matrix and R, an upper
	triangular matrix such that A = QR"""

	n = len(A)

	R = A
	Q = [[0.0] *n for i in xrange(n)]

	for k in range(n-1):
		I = [[float(i==j) for i in xrange(n)] for j in xrange(n)]
		x = [row[k] for row in R[k:]]
		e = [row[k] for row in I[k:]]

		alpha = -cmp(x[0], 0) * norm(x)

		u = map(lambda p, q: p + alpha * q, x, e)
		norm_u = norm(u)
		v = map(lambda p: p/norm_u, u)
		Q_min = [ [float(i==j) - 2.0 * v[i] * v[j] for i in xrange(n-k)] for j in xrange(n-k) ]
		Q_t = [[ Q_i(Q_min,i,j,k) for i in xrange(n)] for j in xrange(n)]

		if k == 0:
			Q = Q_t
			R = mult_matrix(Q_t, A)
		else:
			Q = mult_matrix(Q_t, Q)
			R = mult_matrix(Q_t, R)
	
	return trans_matrix(Q), R

if __name__ == "__main__":
	A = [[12, -51, 4], [6, 167, -68], [-4, 24, -41]]
	Q, R = householder(A)

	print "A:"
	pprint(A)

	print "Q:"
	pprint(Q)
		
	print "R:"
	pprint(R)
