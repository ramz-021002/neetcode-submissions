class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # strMap = {}
        # for str in strs:
        #     key = tuple(sorted(Counter(str).items()))
        #     if key in strMap:
        #         strMap[key].append(str)
        #     else:
        #         strMap[key] = [str]
            
        # return list(strMap.values())

        # strMap = {}
        # for str in strs:
        #     count = [0] * 26
        #     for char in str:
        #         count[ord(char) - ord('a')] += 1
            
        #     key = tuple(count)

        #     if key not in strMap:
        #         strMap[key] = []

        #     strMap[key].append(str)

        # return list(strMap.values())

        strMap = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for c in str:
                count[ord(c) - ord('a')] += 1
            
            strMap[tuple(count)].append(str)
        
        return list(strMap.values())
