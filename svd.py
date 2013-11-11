#http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.svd.html
a = np.random.randn(9, 6) + 1j*np.random.randn(9, 6)
U, s, V = np.linalg.svd(a, full_matrices=True)

U.shape, V.shape, s.shape
S = np.zeros((9, 6), dtype=complex)

S[:6, :6] = np.diag(s)
np.allclose(a, np.dot(U, np.dot(S, V)))

U, s, V = np.linalg.svd(a, full_matrices=False)
U.shape, V.shape, s.shape
S = np.diag(s)

np.allclose(a, np.dot(U, np.dot(S, V)))
