class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idxMap = {}

        for i in range(len(nums)):
            idxMap[nums[i]] = i
        
        #existence of complementary
        for i in range(len(nums)):
            need = target - nums[i]
            if need in idxMap and idxMap[need] != i :
                return [i, idxMap[need]]