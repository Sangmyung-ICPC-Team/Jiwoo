# N-Queen
def isPossible(row):
    for i in range(row):
        if selected[row] == selected[i] or abs(selected[row]-selected[i]) == row-i:
            return False
    return True

def dfs(curr_row):
    global ans
    if curr_row == n:
        ans += 1
    else:
        for col in range(n):
            selected[curr_row] = col
            if isPossible(curr_row):
                dfs(curr_row+1)

n = int(input())
selected = [0]*n
ans = 0

dfs(0)
print(ans)