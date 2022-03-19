from PIL import Image
from math import isclose
import numpy as np

IMAGE_WIDTH = 800
IMAGE_HEIGHT = 800
DOMAIN = (-10, 10)
RANGE = (-10, 10)
RADIUS = 6
SHOW_AXES = True
DO_FILL = True

x_scale = (DOMAIN[1] - DOMAIN[0]) / IMAGE_WIDTH
y_scale = (RANGE[1] - RANGE[0]) / IMAGE_HEIGHT
# I'm not sure if this is correct
x_translation = DOMAIN[0]
y_translation = RANGE[0]

pixels = [] 

for image_y in range(0, IMAGE_HEIGHT + 1):
    y = image_y * y_scale + y_translation
    row = []
    for image_x in range(0, IMAGE_WIDTH + 1):
        x = image_x * x_scale + x_translation
        if SHOW_AXES and (isclose(x, 0, abs_tol=0.01) or isclose(y, 0, abs_tol=0.01)):
            colour = (0, 0, 0)
        elif isclose(x ** 2 + y ** 2, RADIUS ** 2, abs_tol=0.7):
            colour = (255, 0, 0)
        elif DO_FILL and x ** 2 + y ** 2 < RADIUS ** 2:
            colour = (255, 130, 130)
        else:
            colour = (255, 255, 255)
        row.append(colour)
    pixels.append(row)

# Because y is flipped
pixels.reverse()

graph = Image.fromarray(np.array(pixels, dtype=np.uint8))

graph.show()
