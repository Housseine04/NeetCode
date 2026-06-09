
class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0 : 
            return "noInputRetrieved"
        encoded = ""
        for i in range(len(strs)):
            if i == len(strs) - 1:
                encoded += strs[i]
            else:
                encoded += strs[i] + "<br>"
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "noInputRetrieved":
            return []
        decoded = s.split("<br>")
        return decoded

