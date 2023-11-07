import numpy as np

# projection of v on u
def project(u, v):
    return np.dot(np.dot(u.T, v) / np.dot(u.T, u), u) 

def gram_schmidt(vectors):
    for i in range(vectors.shape[0]):
        for j in range(i):
            vectors[i] -= project(vectors[j], vectors[i])

    row_norms = np.linalg.norm(vectors, axis=1)
    vectors /= row_norms[:, np.newaxis]
    return vectors




n, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]

vectors = np.asarray(A, dtype=float)
orthonormal_vectors = gram_schmidt(vectors) 

        
    

   