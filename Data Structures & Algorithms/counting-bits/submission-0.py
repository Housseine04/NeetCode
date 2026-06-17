class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            binary = bin(i)[2:]
            output.append(self.countOnes(binary))
        return output 

    def countOnes(self,n : str) -> int:
        ones = 0
        for char in range(len(n)):
            if(n[char] == "1") : ones += 1
        return ones
