class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i<len(word) and j<len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue
            k = j
            if j<len(abbr) and (abbr[j] == '0' or abbr[j].isalpha()):
                return False
            while j<len(abbr) and  abbr[j].isdigit():
                j += 1
            count = int(abbr[k:j])
            i += count
        return i == len(word) and j == len(abbr)