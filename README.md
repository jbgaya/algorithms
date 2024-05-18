## Problem: Dot Product of Sparse Vectors

You are given two sparse vectors, each represented as a list of tuples. Each tuple contains an index and a value, representing non-zero entries of the vector.

Write a function to compute the dot product of these two sparse vectors. The dot product is defined as the sum of the products of corresponding entries.

### Function Signature

```python
def dot_product(vec1: tp.List[tp.Tuple[int, float]], vec2: tp.List[tp.Tuple[int, float]]) -> float:
    # Your implementation here
    pass
```

### Example

```python
vec1 = [(0, 1.0), (3, 2.0), (4, 3.0)]
vec2 = [(0, 4.0), (2, 1.0), (4, 2.0)]
print(dot_product(vec1, vec2))  # Output should be 10.0 (1.0*4.0 + 3.0*2.0)
```

### Constraints

* The indices in the tuples are unique within each vector.
* Vectors can be of different lengths.
* Indices are not guaranteed to be sorted.