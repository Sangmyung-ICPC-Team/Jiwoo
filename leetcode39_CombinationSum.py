class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def solve(subset, idx, total):
            if total == target:
                answer.append(subset)
            else:
                for i in range(idx, len(candidates)):
                    if total + candidates[i] > target:
                        break
                    else:
                        solve(subset + [candidates[i]], i, total + candidates[i])

        candidates.sort()
        answer = list()

        solve([], 0, 0)

        return answer