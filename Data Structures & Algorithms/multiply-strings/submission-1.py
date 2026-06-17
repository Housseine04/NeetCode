class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = [0] * (len(num1) + len(num2))
        num1 = num1[::-1]
        num2 = num2[::-1]

        start_addition = 0
        for d1 in range(len(num1)):
            currIndex = start_addition
            for d2 in range(len(num2)):
                result[currIndex] += int(num1[d1]) * int(num2[d2])
                currIndex += 1
            start_addition += 1
        remainder = 0
        for i in range(len(result)):
            currentSum = result[i] + remainder
            if currentSum > 9:
                result[i] = currentSum % 10
            else:
                result[i] = currentSum
            remainder = currentSum // 10

        result = result[::-1]
        return "".join(map(str, result)).lstrip("0") or "0"