import numpy as np
import matplotlib.pyplot as plt

def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1

size = 100
image = np.zeros((size, size, 3), dtype="uint8")
print(image)
assert image.shape[0] == image.shape[1]

color1 = [189, 238, 252]
color2 = [241, 141, 242]

for y in range(size):
    for x in range(size):
        right_pos = (y + x) / (2 * (size - 1))
        r = int(lerp(color1[0], color2[0], right_pos))
        g = int(lerp(color1[1], color2[1], right_pos))
        b = int(lerp(color1[2], color2[2], right_pos))
        image[y, x, :] = [r, g, b]

plt.figure(1)
plt.imshow(image)
plt.show()