class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for i in range(len(nums)+1):
            xor = xor ^ i #0 ^ 1 ^ 2 ...
        for i in range(len(nums)):
            xor = xor ^ nums[i] #if present then eliminated by XOR 
        return xor
        