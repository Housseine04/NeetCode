class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = 0
        nums.sort()
        for i in nums:
            if expected != i:
                return expected
            expected += 1
        return expected
        