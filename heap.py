import typing as tp

real = int | float

class binaryTree:
    def __init__(self, val: tp.Any):
        if not isinstance(val, real):
            assert hasattr(val[0], "__eq__") and hasattr(val[0], "__lt__") and hasattr(val[0], "__gt__"), f"the type of object {type(val[0])} you're trying to push has no comparison attributes."
        self.val: tp.Any = val
        self.left: tp.Optional[binaryTree] = None
        self.right: tp.Optional[binaryTree] = None

    def __lt__(self, b: 'binaryTree') -> bool:
        assert type(self.val) == type(b.val), f"Trees don't have the same type: {type(self.val)} and {type(b.val)}"

        if isinstance(self.val, real):
            return self.val < b.val
        else:
            return self.val[0] < b.val[0]

    def __eq__(self, b: 'binaryTree') -> bool:
        assert type(self.val) == type(b.val), f"Trees don't have the same type: {type(self.val)} and {type(b.val)}"

        if isinstance(self.val, real):
            return self.val == b.val
        else:
            return self.val[0] == b.val[0]
        
    def __le__(self, b: 'binaryTree') -> bool:
        assert type(self.val) == type(b.val), f"Trees don't have the same type: {type(self.val)} and {type(b.val)}"

        if isinstance(self.val, real):
            return self.val <= b.val
        else:
            return self.val[0] <= b.val[0]

    def __ge__(self, b: 'binaryTree') -> bool:
        assert type(self.val) == type(b.val), f"Trees don't have the same type: {type(self.val)} and {type(b.val)}"

        if isinstance(self.val, real):
            return self.val >= b.val
        else:
            return self.val[0] >= b.val[0]

    def __gt__(self, b: 'binaryTree') -> bool:
        assert type(self.val) == type(b.val), f"Trees don't have the same type: {type(self.val)} and {type(b.val)}"

        if isinstance(self.val, real):
            return self.val > b.val
        else:
            return self.val[0] > b.val[0]

    def __call__(self) -> tp.List[tp.Any]:
        left_part = [] if self.left is None else self.left.__call__()
        right_part = [] if self.right is None else self.right.__call__()
        return left_part + [self.val] + right_part

    def __str__(self) -> str:
        return str(self.__call__())

    def __repr__(self) -> str:
        return str(self.__call__())



class Heap:
    def __init__(self, max_length: real = float("inf")):
        self.root: tp.Optional[binaryTree] = None
        self.max_length: real = max_length
        self.length: int = 0

        self._index: int = 0  # To keep track of the current node in iteration
        self._elements: tp.List[tp.Any] = []  # To store elements for iteration

    def __len__(self):
        return self.length

    def push(self,val: tp.Any) -> None:
        if not isinstance(val,binaryTree):
            val = binaryTree(val)

        if self.root is None:
            self.root = val
            self.length += 1
        elif self.length == self.max_length:
            print(f"maximum length reached ({self.max_length}), use .pushpop instead.")
        else:
            current_heap = self.root
            while True:
                if val <= current_heap:
                    if current_heap.left is None:
                        current_heap.left = val
                        break
                    else:
                        current_heap = current_heap.left
                else:
                    if current_heap.right is None:
                        current_heap.right = val
                        break
                    else:
                        current_heap = current_heap.right
            self.length += 1

    def pushpop(self,val: tp.Any) -> tp.Optional[tp.Any]:
        """
        Try to push val and pop the smallest element of the heap
        """
        if not isinstance(val,binaryTree):
            val = binaryTree(val)
        # handling the case where we don't need to pop anything
        if self.length < self.max_length:
            self.push(val)
            return None
        
        #popping the smallest element
        current_heap = self.root
        if self.root.left is None and val > self.root:
            val_to_pop = self.root.val
            self.root = self.root.right
        else:
            val_to_pop = val.val
            while current_heap.left is not None:
                parent_heap = current_heap
                current_heap = current_heap.left
            if val > current_heap:
                val_to_pop = current_heap.val
                parent_heap.left = current_heap.right
                self.length -= 1
                self.push(val)
        return val_to_pop
    
    def sort(self) -> tp.List[real]:
        """
        return the sorted elements of the heap
        """
        sorted_list = []
        if self.root:
            sorted_list = self.root()
        return sorted_list

    
    def __call__(self):
        if self.root is None:
            return []
        return self.root.__call__()
    
    def __str__(self):
        return str(self.__call__())
        
    def __repr__(self):
        return str(self.__call__())

    def __iter__(self):
        # Flatten the tree into a list
        self._elements = self.sort() if self.root else []
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._elements):
            result = self._elements[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration()