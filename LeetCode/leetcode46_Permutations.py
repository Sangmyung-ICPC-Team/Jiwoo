# https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(permut):
            if len(permut) == len(nums):
                answer.append(permut)
            else:

                for i in range(len(nums)):
                    if not selected[i]:
                        selected[i] = True
                        dfs(permut + [nums[i]])
                        selected[i] = False

        selected = [False] * (len(nums))

        answer = []

        dfs([])

        return answer
