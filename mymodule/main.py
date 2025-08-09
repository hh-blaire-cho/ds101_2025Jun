import apple
import orange
import numpy as np
import mymath as mm

print("hello main")

arr1 = np.array([11, 12, 13])
arr2 = np.array([11, 11.5, 12, 12.5, 13, 13.5])
x1 = mm.MyMath(999, "Rose")
x2 = mm.MyMath(1000, "Lisa")

print(arr1.shape)
print(arr1.max())
print(arr2.shape)
print(arr2.max())

print("-"*100)

print(x1.name)
print(x1.is_bigger_than(50))
print(x1.is_bigger_than(101))

print("-"*100)

print(x2.name)
print(x2.is_bigger_than(500))
print(x2.is_bigger_than(1500))
