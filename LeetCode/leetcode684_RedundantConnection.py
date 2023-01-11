from collections import defaultdict as dd

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def has_cycle(v1, v2):
            '''
            v2부터 dfs탐색하여 v1으로 돌아올 수 있다면 cycle 존재 -> True
            '''

            visited = [False] * (n + 1)
            ### 탐색을 위해 visited[v1]를 True 처리해두지 않음

            s = [v2]
            prev = v1

            while s:
                curr = s.pop()
                visited[curr] = True

                if curr == v1 and v1 != prev:  # 다시 v1으로 돌아왔다면
                    return True

                for adj in graph[curr]:
                    if not visited[adj]:
                        s.append(adj)

                prev = curr  # prev 갱신

            return False

        n = len(edges)
        graph = dd(list)

        for s, e in edges:  # 해당 edge를 추가해서 사이클이 생긴다면
            if has_cycle(s, e):
                return s, e

            # 사이클이 생기지 않는다면 각 정점의 이웃으로 추가
            graph[s].append(e)
            graph[e].append(s)
