# 행렬
n, m = map(int, input().split())

a_matrix = [list(map(int, list(input()))) for _ in range(n)]
b_matrix = [list(map(int, list(input()))) for _ in range(n)]

def transposeMatrix(x, y):
  for i in range(x, x+3):
    for j in range(y, y+3):
      if b_matrix[i][j] == 0:
        b_matrix[i][j] = 1
      else:
        b_matrix[i][j] = 0

cnt = 0
for curr_x in range(n-2):
  for curr_y in range(m-2):
    if a_matrix[curr_x][curr_y] != b_matrix[curr_x][curr_y]:
      cnt += 1
      transposeMatrix(curr_x, curr_y)
      
isEqual = True
for i in range(n):
  for j in range(m):
    if a_matrix[i][j] != b_matrix[i][j]:
      isEqual = not isEqual
      break
  if not isEqual:
    break
    
if isEqual:
  print(cnt)
else:
  print(-1)