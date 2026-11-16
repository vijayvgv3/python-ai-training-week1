import numpy as np

marks = np.array([
    [70, 80, 90],
    [60, 75, 85],
    [88, 92, 79],
    [55, 65, 70]
])


print("shape:", marks.shape)
print("dtype:", marks.dtype)
print("Size:", marks.size)

print("sliced:", marks[:2, -1])

print("student average:", np.round(np.mean(marks, axis=1), 2))
print("subject average:", np.round(np.mean(marks, axis=0), 2))

grace_marks = marks + 5
print("Grace marks:\n", grace_marks)

weights = [0.3, 0.3, 0.4]
print("weighted scores:", np.dot(marks, weights))

reshaped = np.arange(12).reshape(3, 4)
print("Reshaped:\n", reshaped)
