import typing as tp
import random
import time

def move_zero_to_end(arr: tp.List) -> tp.List:
    for i in range(len(arr)-1):
        if arr[i] == 0:
            for j in range(i+1,len(arr)):
                if arr[j] != 0:
                    arr[i],arr[j] = arr[j],arr[i]
                    break
    return arr

def move_zero_to_end_v2(arr: tp.List) -> tp.List:
    for i in range(len(arr)-1):
        if arr[i] == 0:
            for j in range(i+1,len(arr)):
                if arr[j] != 0:
                    arr[i],arr[j] = arr[j],arr[i]
                    break
            i = j+1
    return arr

def move_zero_to_end_optimized(arr:tp.List) -> tp.List:
    write = 0
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write] = arr[read]
            write += 1
    
    for i in range(write,len(arr)):
        arr[i] = 0

    return arr

def move_zero_to_end_cleanest(arr:tp.List) -> tp.List:
    write = 0 
    for read in range(len(arr)):
        if arr[read] != 0:
            arr[write],arr[read] = arr[read],arr[write]
            write+=1
    return arr


def create_sparse_array(n: int, sparsity: float = 0.5) -> tp.List[float]:
    """
    Create a sparse vector with n elements. Sparsity is the probability of having a non-zero value.
    """
    return [random.randint(1,10) if random.random() > sparsity else 0.0 for _ in range(n)]


if __name__ == "__main__":
    # Toy example
    arr = [0, 1, 0, 3, 12]
    print(move_zero_to_end(arr))

    # Comparing to classical dot product with two vectors that are 90% sparse
    n = 10_000_000
    sparsity = 0.99
    arr = create_sparse_array(n, sparsity)

    # Testing baseline
    if n <= 10_000:
        start = time.time()
        arr2 = move_zero_to_end(arr)
        stop = time.time()
        print(f"Naive baseline: {stop-start:.2f} sec")

        # Testing v2
        start = time.time()
        arr2 = move_zero_to_end_v2(arr)
        stop = time.time()
        print(f"Naive baseline v2: {stop-start:.2f} sec")

    # Testing optimized
    start = time.time()
    arr2 = move_zero_to_end_optimized(arr)
    stop = time.time()
    print(f"Optimized: {stop-start:.2f} sec")

    # Testing cleanest
    start = time.time()
    arr2 = move_zero_to_end_cleanest(arr)
    stop = time.time()
    print(f"Cleanest: {stop-start:.2f} sec")