import numpy as np

print("=== Exercise 1 : Array Creation ===")
arr1 = np.arange(10)
print(arr1)

print("\n=== Exercise 2 : Type Conversion ===")
arr2 = np.array([3.14, 2.17, 0, 1, 2]).astype(int)
print(arr2)

print("\n=== Exercise 3 : Multi-Dimensional Array ===")
arr3 = np.arange(1, 10).reshape(3, 3)
print(arr3)

print("\n=== Exercise 4 : Random Array (4x5) ===")
arr4 = np.random.rand(4, 5).round(2)
print(arr4)

print("\n=== Exercise 5 : Indexing - Second Row ===")
arr5 = np.array([[21,22,23,22,22],[20,21,22,23,24],[21,22,23,22,22]])
print(arr5[1])

print("\n=== Exercise 6 : Reversing Elements ===")
arr6 = np.arange(10)
print(arr6[::-1])

print("\n=== Exercise 7 : Identity Matrix (4x4) ===")
arr7 = np.eye(4)
print(arr7)

print("\n=== Exercise 8 : Sum and Average ===")
arr8 = np.arange(10)
print(f"Sum: {arr8.sum()}, Average: {arr8.mean()}")

print("\n=== Exercise 9 : Reshape (4x5) ===")
arr9 = np.arange(1, 21).reshape(4, 5)
print(arr9)

print("\n=== Exercise 10 : Odd Numbers ===")
arr10 = np.arange(1, 10)
print(arr10[arr10 % 2 != 0])
