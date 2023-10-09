import numpy as np
from timeit import timeit
from pysample import fib, matmul
from pysample import cpp_impl, rust_impl


n = 30
RUNS = 10
print(f"{fib(n)           = }")
print(f"{cpp_impl.fib(n)  = }")
print(f"{rust_impl.fib(n) = }")

python_time_per_call = timeit(lambda: fib(n), number=RUNS) / RUNS
print(f"Python ms per call: {python_time_per_call * 1_000:.2f} ms")

cpp_time_per_call = timeit(lambda: cpp_impl.fib(n), number=RUNS) / RUNS
print(f"C++ ms per call: {cpp_time_per_call * 1_000:.2f} ms")

rust_time_per_call = timeit(lambda: rust_impl.fib(n), number=RUNS) / RUNS
print(f"Rust ms per call: {rust_time_per_call * 1_000:.2f} ms")


a = np.random.rand(100, 2000)
b = np.random.rand(2000, 100)
p = matmul(a, b)
c = cpp_impl.matmul(a, b)
r = rust_impl.matmul(a, b)
print()
print(f"{np.allclose(p, c) = }")
print(f"{np.allclose(p, r) = }")

python_time_per_call = timeit(lambda: matmul(a, b), number=RUNS) / RUNS
print(f"Python ms per call: {python_time_per_call * 1_000:.2f} ms")

cpp_time_per_call = timeit(lambda: cpp_impl.matmul(a, b), number=RUNS) / RUNS
print(f"C++ ms per call: {cpp_time_per_call * 1_000:.2f} ms")

rust_time_per_call = timeit(lambda: rust_impl.matmul(a, b), number=RUNS) / RUNS
print(f"Rust ms per call: {rust_time_per_call * 1_000:.2f} ms")
