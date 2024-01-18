import numpy as np

print("Python List Operations:")
a = [1,2,3]
b = [4,5,6]
print("a + b = ", a+b)
try:
    print(a*b)
except TypeError:
    print("a * b has no meaning in Python Lists")
print()

print("NumPy Array Operations:")
a = np.array