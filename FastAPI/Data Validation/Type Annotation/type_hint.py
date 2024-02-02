# Variable Annotation
a: int = 1
b: int = 1

# Function Annotation
def add(a: int, b: int) -> int:
    return a + b

# List Annotation
from typing import List
arr: List[List[int]] = [[1, 2], [3, 4]]
print(arr)
arr0: list[list[int]] = [[1, 2], [3, 4]]
print(arr0)

# Dict Annotation
from typing import Dict
x: Dict[str, int] = {'field': 2}
print(x)
x0: dict[str, int] = {'field': 2}
print(x0)

# Set Annotation
from typing import Set
y: Set[int] = {1, 2, 3}
print(y)
y0: set[int] = {1, 2, 3}
print(y0)

# Custom Annotation
Vector = List[float]
def foo(v: Vector) -> Vector:
    return v

Vectors = List[Vector]
def bar(v: Vectors) -> Vectors:
    return v

# Optional Annotation
from typing import Optional
def foo(output: Optional[bool]=False):
    pass
def bar(output: bool=False):
    pass

# Any Annotation
from typing import Any
def foo(output: Any):
    pass

# Sequence Annotation
from typing import Sequence
def foo(seq: Sequence[int]):
    pass
foo([1, 2, 3])
foo((1, 2, 3))

# Tuple Annotation
from typing import Tuple
x: Tuple[int, str, float] = (1, 'a', 1.0)

# Callable Annotation
from typing import Callable
def add(a: int, b: int) -> int:
    return a + b
def foo(func: Callable[[int, int, Optional[int]], int]) -> None:
    func(1, 2)
foo(add)

def foo() -> Callable[[int, int], int]:
    def add(a: int, b: int) -> int:
        return a + b
    return add
foo()

# Generics
from typing import TypeVar
T = TypeVar('T')
def get_item(list: List[T], index: int) -> T:
    return list[index]