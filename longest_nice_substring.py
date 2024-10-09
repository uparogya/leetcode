class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        content = set(s)

        for i in range(len(s)):
            if s[i].lower() in content and s[i].upper() in content:
                continue

            left_string = self.longestNiceSubstring(s[:i])
            right_string = self.longestNiceSubstring(s[i+1:])
            return max(left_string, right_string, key=len)
            
        return s


solution = Solution().longestNiceSubstring("YazaAay")
print(solution)