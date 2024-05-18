import typing as tp
import time 
import random

def dot_product(vec1: tp.List[tp.Tuple[int, float]], vec2: tp.List[tp.Tuple[int, float]]) -> float:
    """
    Perform dot product on two sparse vectors that only contain non-zero values.
    
    Time Complexity: O(n1 + n2)
    Memory Complexity: O(min(n1, n2))
    """
    # Ensure vec1 is the smaller vector for dictionary conversion to minimize memory usage
    if len(vec1) > len(vec2):
        vec1, vec2 = vec2, vec1

    # Instantiate a variable for the sum and a dictionary for storing the values of the first vector
    sum: float = 0
    dict_vec1: tp.Dict[int, float] = {idx1: x1 for idx1, x1 in vec1}

    # Iterate through vec2 and add to sum the product when indexes match using the dictionary
    for idx2, x2 in vec2:
        if idx2 in dict_vec1:
            sum += dict_vec1[idx2] * x2
    return sum

def create_sparse_vector(n: int, sparsity: float = 0.5, max_value: float = 10_000.0) -> tp.List[float]:
    """
    Create a sparse vector with n elements. Sparsity is the probability of having a non-zero value.
    """
    return [random.random() * max_value if random.random() > sparsity else 0.0 for _ in range(n)]

def sparsify(vec: tp.List[float]) -> tp.List[tp.Tuple[int, float]]:
    """
    Transform a dense vector into a sparse vector.
    """
    return [(i, x) if x != 0.0 else (i, 0.0) for i, x in enumerate(vec)]

if __name__ == "__main__":

    # Toy example
    vec1 = [(0, 1.0), (3, 2.0), (4, 3.0)]
    vec2 = [(0, 4.0), (2, 1.0), (4, 2.0)]
    print(dot_product(vec1, vec2))

    # Comparing to classical dot product with two vectors that are 90% sparse
    n = 1_000_000
    sparsity = 0.9
    vec1 = create_sparse_vector(n, sparsity)
    vec2 = create_sparse_vector(n, sparsity)

    # Testing baseline
    start = time.time()
    sum: float = 0.0
    for x1, x2 in zip(vec1, vec2):
        sum += x1 * x2
    stop = time.time()
    print(f"Naive baseline: {stop-start:.2f} sec")

    # Testing our sparse dot product
    vec1_sparse = sparsify(vec1)
    vec2_sparse = sparsify(vec2)
    start = time.time()
    sum = dot_product(vec1_sparse, vec2_sparse)
    stop = time.time()
    print(f"Sparse dot product: {stop-start:.2f} sec")