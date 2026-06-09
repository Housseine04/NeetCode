class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print("initial : ", nums)
        result = [0] * len(nums)
        result[0] = 1
        multip = 1
        for i in range(1, len(nums)):  # left to right
            multip *= nums[i-1]
            result[i] = multip
        print("frist pass : ", result)
        multip = 1
        for i in range(len(nums)-1, 0, -1):
            multip *= nums[i]
            result[i-1] *= multip
        print(result)
        return result