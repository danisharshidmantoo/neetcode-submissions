class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s))+"#"+s)
        
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0
        while i<len(s):
            #skip # and the length
            k = i
            while s[k]!='#':
                k += 1
            leng = int(s[i:k])
            i = k + 1
            output.append(s[i:i+leng])
            i = i+leng
        return output