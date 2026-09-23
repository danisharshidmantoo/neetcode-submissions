class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            output += str(len(s)) + "#" + s
        return output
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i<len(s):
            #extract length
            length = ""
            while s[i]!="#":
                length += s[i]
                i += 1
            i += 1
            result.append(s[i:i+int(length)])
            i += int(length)
        return result