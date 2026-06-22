class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0 : return False
        stack = []
        for i in list(s):
            if i == '(' or i == '[' or i =='{':
                stack.append(i)
            else:
                if len(stack) == 0: return False
                else:
                    last = stack.pop()
                    if last == '(' and i != ')': return False
                    elif last == '[' and i != ']': return False
                    elif last == '{' and i != '}': return False
        return len(stack) == 0

        