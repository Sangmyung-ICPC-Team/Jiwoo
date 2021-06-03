# N과 M(1)
def get_possible_seq(length):
    if length == m:
        print(*seq)
    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                seq.append(i+1)
                get_possible_seq(length+1)
                seq.pop()
                visited[i] = False

seq = []
n, m = map(int, input().split())
visited = [False for _ in range(n)]
get_possible_seq(0)