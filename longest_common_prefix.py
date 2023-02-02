class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        thisDict = {}
        for index in range(len(strs)):
            thisSet = set()
            concatCharacters = ''
            for thisChar in strs[index]:
                concatCharacters += thisChar
                thisSet.add(concatCharacters)
            thisDict[index] = thisSet
        
        baseSet = thisDict[0]
        newSet = set()
        for index in range(1,len(thisDict)):
            newSet = baseSet.intersection(thisDict[index])
            baseSet = newSet

        baseSet = list(baseSet)
        if len(baseSet) == 0: return ''

        longestCommonPrefix = baseSet[0]
        for prefix in baseSet:
            if len(prefix) > len(longestCommonPrefix):
                longestCommonPrefix = prefix
    
        return longestCommonPrefix

strs = ["account", "access", "acting", "acer", "ace"]
print(Solution().longestCommonPrefix(strs))