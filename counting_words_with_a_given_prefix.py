class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0
        for word in words:
            if pref in word:
                for index, letter in enumerate(pref):
                    if letter != word[index]:
                        count -= 1
                        break

                count += 1

        return count