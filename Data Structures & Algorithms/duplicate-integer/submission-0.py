class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashnums = {}
        for num in nums:
            if num in hashnums:
                return True
            hashnums[num] = 1
        return False

        