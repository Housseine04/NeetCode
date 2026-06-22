class Solution:
    def isPalindrome(self, s: str) -> bool:
        start , end = 0 , len(s)-1
        while start <= end :
            charStart = s[start]
            charEnd = s[end]
            if not charStart.isalnum():
                start += 1
                continue
            if not charEnd.isalnum():
                end -= 1
                continue

            if charStart.isnumeric() :
                if not charEnd.isnumeric() or charStart != charEnd : return False
            else:
                if charStart.lower() != charEnd.lower() : return False
            end -= 1
            start += 1
        return True
