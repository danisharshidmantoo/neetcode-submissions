class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for s in strs:
            result.append(str(len(s))+"#"+s)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        output = []
        n = len(s)
        i = 0 # for traversing the string
        j = 0 # for getting the length
        while i<n:
            #get the length
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            output.append(s[i:i+length])
            i += length
           
        return output