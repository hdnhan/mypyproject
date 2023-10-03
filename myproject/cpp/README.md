## Build python binding for C++ code
```bash
cmake . -B build
cmake --build build
```

## Test
```python
>>> from build import multiply_cpp_impl
>>> import numpy as np
>>> a = np.random.rand(100, 200)
>>> b = np.random.rand(200, 300)
>>> c = multiply_cpp_impl.multiply_cpp(a, b)
>>> d = np.matmul(a, b)
>>> np.abs(c - d).max()
4.583103306998737e-05
```