import math
import random

def move_up():
  for i in range(3, 0, -1):
    for j in range(0, 4):
      if matrix[i][j] != 0:
        if matrix[i-1][j] == 0:
          matrix[i-1][j] = matrix[i][j]
          matrix[i][j] = 0
          continue
        if matrix[i-1][j] == matrix[i][j]:
          matrix[i-1][j] *= 2
          matrix[i][j] = 0
          
def move_down():
  for i in range(0, 3):
    for j in range(0, 4):
      if matrix[i][j] != 0:
        if matrix[i+1][j] == 0:
          matrix[i+1][j] = matrix[i][j]
          matrix[i][j] = 0
          continue
        if matrix[i+1][j] == matrix[i][j]:
          matrix[i+1][j] *= 2
          matrix[i][j] = 0
          
def move_left():
  for i in range(0, 4):
    for j in range(3, 0, -1):
      if matrix[i][j] != 0:
        if matrix[i][j-1] == 0:
          matrix[i][j-1] = matrix[i][j]
          matrix[i][j] = 0
          continue
        if matrix[i][j-1] == matrix[i][j]:
          matrix[i][j-1] *= 2
          matrix[i][j] = 0
          
def move_right():
  for i in range(0, 4):
    for j in range(0, 3):
      if matrix[i][j] != 0:
        if matrix[i][j+1] == 0:
          matrix[i][j+1] = matrix[i][j]
          matrix[i][j] = 0
          continue
        if matrix[i][j+1] == matrix[i][j]:
          matrix[i][j+1] *= 2
          matrix[i][j] = 0

(w, h) = (4, 4);

matrix = [[0 for x in range(w)] for y in range(h)]


matrix[random.randint(0,3)][random.randint(0,3)]=2

while True:
  x=random.randint(0,3)
  y=random.randint(0,3)
  if matrix[x][y]==0:
    matrix[x][y]=2
    break

while True:
  for i in range(h):
    print(matrix[i])
  
  g=input()
  if g == "w":
    move_up()
  elif g == "s":
    move_down()
  elif g == "a":
    move_left()
  elif g == "d":
    move_right()
  
  while True:
    x=random.randint(0,3)
    y=random.randint(0,3)
    r = random.randint(0, 6)
    if matrix[x][y]==0:
      if r == 0:
        matrix[x][y] = 4
      else:
        matrix[x][y] = 2
      break
          
          