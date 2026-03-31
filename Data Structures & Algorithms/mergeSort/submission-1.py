# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        list1 = self.mergeSort(pairs[:len(pairs)//2])
        list2 = self.mergeSort(pairs[(len(pairs)//2):])
        merged = []

        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i].key <= list2[j].key:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
                
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        return merged
    
        