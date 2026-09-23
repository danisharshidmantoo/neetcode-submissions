class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s))+"#"+s)
        return ''.join(res)
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            result.append(s[j+1:j+1+l])
            i = j + 1 + l
        return result
             