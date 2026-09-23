class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s))+'#' + s
        return output
    def decode(self, s: str) -> List[str]:
        ans = []
        cur = ""
        i = 0
        
        while i<len(s):
            j = i
            while j<len(s) and s[j]!='#':
                j += 1
            curLen = int(s[i:j])
            ans.append(s[j+1:j+1+curLen])
            i = j+1+curLen
             
        return ans