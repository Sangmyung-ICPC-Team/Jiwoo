class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        stack = []

        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if not stack:
                    cnt += 1
                else:
                    stack.pop()

        cnt += len(stack)
        return cnt