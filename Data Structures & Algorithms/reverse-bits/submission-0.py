class Solution:
    def reverseBits(self, n: int) -> int:
        result = [0] * 32
        nString = str(bin(n))[2:]
        for i in range(len(nString) - 1, -1, -1):
            result[len(nString) - i - 1] = int(nString[i])

        reversedBin = "".join(map(str, result))
        return int(reversedBin,2)
