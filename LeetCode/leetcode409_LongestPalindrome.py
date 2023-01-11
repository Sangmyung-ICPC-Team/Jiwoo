# https://leetcode.com/problems/longest-palindrome/
class Solution:
    def longestPalindrome(self, s: str) -> int:

        char_nums = defaultdict(int)

        for c in s:
            char_nums[c] += 1

        pq = []

        for c, n in char_nums.items():
            heapq.heappush(pq, (-n, n, c))

        answer = 0

        while pq:
            _, n, c = heapq.heappop(pq)

            if not answer & 1:  # when answer is even
                answer += n
            elif n >= 2:  # when answer is odd and n is even larger than 2
                answer += n - 1 if n & 1 else n

        return answer