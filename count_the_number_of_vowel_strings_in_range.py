class Solution:
    def vowelStrings(self, words: list[str], left: int, right: int) -> int:
        vowels = ['a','e','i','o','u']
        vowelStrings = 0

        for i in range(left, right + 1):
            thisWordStart = words[i] [0]
            thisWordEnd = words[i] [-1]
            if thisWordStart in vowels and thisWordEnd in vowels:
                vowelStrings += 1
            
        return vowelStrings


words = ["hey","aeo","mu","ooo","artro"]
left = 1
right = 4
print(Solution().vowelStrings(words,left,right))