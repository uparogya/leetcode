class Solution:
    def canConstruct(s: str, k: int) -> bool:
        if k > len(s):
            return False

        character_count = {}
        even_count = 0

        for char in s:
            if char not in character_count:
                character_count[char] = 1
            else:
                character_count[char] += 1
            
            if character_count[char] == 2:
                even_count += 1
                character_count[char] = 0

        odd_count = max(0 , len(s) - (2*even_count))

        if odd_count == 0:
            return True
        
        if odd_count > k:
            return False
        
        return True

print(Solution.canConstruct("annabelle", 2))