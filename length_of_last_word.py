class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        strArray = s.split()
        return len(strArray[-1])

s = "Hello World"
print(Solution().lengthOfLastWord(s))