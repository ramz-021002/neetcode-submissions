class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for str in strs:
            key = frozenset(str)

            if key in strMap:
                strMap[key].append(str)
            else:
                strMap[key] = [str]
            
        return list(strMap.values())