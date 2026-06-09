class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapT = {}
        mapS = {}

        for i in range(len(s)):
            if s[i] in mapS:
                mapS[s[i]] += 1
            else:
                mapS[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in mapT:
                mapT[t[i]] += 1
            else:
                mapT[t[i]] = 1
        
        #check
        if len(mapT) != len(mapS):
            return False
        
        for key in mapS:
            if (not key in mapT) or (mapT[key] != mapS[key]) :
                return False
        
        return True

 

        
        