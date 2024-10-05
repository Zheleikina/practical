import numpy as np
import random

A = np.array(random.sample(range(1, 25), 12))

B = A.reshape(3, 4)

print("Одновимірний масив A:", A)
print("Двовимірний масив B:")
print(B)