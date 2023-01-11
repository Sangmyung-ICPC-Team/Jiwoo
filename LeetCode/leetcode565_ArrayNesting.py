class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False for _ in range(len(nums))]
        max_length = 0

        for start in range(len(nums)):
            s = list()
            curr = start
            while not visited[start]:
                s.append(nums[curr])
                curr = nums[curr]
                visited[curr] = True
            max_length = max(max_length, len(s))

        return max_length