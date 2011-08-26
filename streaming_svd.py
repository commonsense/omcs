import numpy as np
import numpy.linalg as LA

# Dimensions
n = 100
c = 1000
m = int(1e3) # dimension of the sign matrix

# Input matrices
A = np.random.standard_normal((n, c))
B = np.random.standard_normal((n, c))

norm_A = LA.norm(A)
norm_B = LA.norm(B)
print 'norm of A', norm_A, 'B', norm_B

# sign (Rademacher) matrices
S = np.random.random_sample((n, m)) * 2
S = S.astype(np.int) * 2 - 1

# Matrix Product
StA = np.dot(S.T, A)
StB = np.dot(S.T, B)
res = np.dot(StA.T, StB) / m
ref = np.dot(A.T, B)
err = LA.norm(res - ref) / (norm_A * norm_B)
print 'Matrix product err', err

# Streaming matrix product
streaming_StA = np.zeros((m, c))
streaming_StB = np.zeros((m, c))
for row in range(n):
    for col in range(c):
        # Apply the update of A[row, col] from 0 to its actual value.
        streaming_StA[:, col] += S[row, :] * A[row, col]

        # Apply the update of B[row, col] from 0 to its actual value.
        streaming_StB[:, col] += S[row, :] * B[row, col]

assert np.allclose(streaming_StA, StA)
assert np.allclose(streaming_StB, StB)

# Linear Regression

# Low-Rank Approximation

