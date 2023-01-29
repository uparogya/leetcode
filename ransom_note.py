class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineList = []
        ransomNoteList = []
        for char in magazine:
            magazineList.append(char)
        for char in ransomNote:
            ransomNoteList.append(char)
            
        mIndex = 0
        while mIndex < len(magazineList):
            if len(ransomNoteList) == 0: break
            rIndex = 0
            while rIndex < len(ransomNoteList):
                loopBroken = False
                if ransomNoteList[rIndex] == magazineList[mIndex]:
                    magazineList.pop(mIndex)
                    ransomNoteList.pop(rIndex)
                    rIndex = 0
                    mIndex = 0
                    loopBroken = True
                    break
                rIndex += 1
            if loopBroken == False: mIndex += 1
        
        return True if len(ransomNoteList) == 0 else False

ransomNote = "ba"
magazine = "abb"
print(Solution().canConstruct(ransomNote,magazine))