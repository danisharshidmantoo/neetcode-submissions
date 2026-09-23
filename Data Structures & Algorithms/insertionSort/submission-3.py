# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        newPairs = []
        if pairs:
            newPairs.append(pairs.copy())
        for i in range(1,len(pairs)):
            
            for j in range(i,0,-1):
                if pairs[j].key < pairs[j-1].key:
                    pairs[j],pairs[j-1] = pairs[j-1],pairs[j]
            newPairs.append(pairs.copy())
        return newPairs