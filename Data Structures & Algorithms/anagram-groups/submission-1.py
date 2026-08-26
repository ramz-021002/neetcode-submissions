class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for str in strs:
            count = Counter(str)
            
            key = tuple(sorted(count.items()))
            if key in strMap:
                strMap[key].append(str)
            else:
                strMap[key] = [str]
            
        return list(strMap.values())