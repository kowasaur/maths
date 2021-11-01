from Matrix import Matrix
from math import cos, sin, radians, sqrt

def dcos(n):
  return round(cos(radians(n)), 12) 

def dsin(n):
  return round(sin(radians(n)), 12)

print(dsin(90))
# og = Matrix(
#   (dcos(150), -dsin(150)),
#   (dsin(150),  dcos(150))
# )
og = Matrix(
  (-sqrt(3)/2, -0.5),
  (0.5,  -sqrt(3)/2)
)
for i in range(1, 13):
  print(i)
  print(round(og ** i, 3))
  print()