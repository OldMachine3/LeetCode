class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtract(curr):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtract(curr)
                    curr.pop()
        
        ans = []
        backtract([])
        return ans