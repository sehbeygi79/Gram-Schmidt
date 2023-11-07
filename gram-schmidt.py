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

def sort_rows(matrix, ascending=True):
    order = 1 if ascending else -1
    sorted_index = [order * matrix[:, i] for i in range(matrix.shape[1]-1, -1, -1)]
    return matrix[np.lexsort(sorted_index)]

def print_matrix(matrix):
    for _, row in enumerate(matrix):
        for elem in row:
            print(f'{elem:.3f} ', end='')
        print()


n, m = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(n)]

vectors = np.asarray(A, dtype=float)
orthonormal_vectors = gram_schmidt(vectors) 
print_matrix(sort_rows(orthonormal_vectors, ascending=False))

        
    

   