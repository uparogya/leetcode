class Solution:
    def stringMatching(words: list[str]) -> list[str]:
        set_words = set(words)
        final_list = set()

        for word in words:
            for i in range(0,len(word)):
                str_1 = word[i]
                if str_1 in set_words and str_1 != word:
                    final_list.add(str_1)
                for j in range(i+1,len(word)):
                    str_1 += word[j]
                    if str_1 in set_words and str_1 != word:
                        final_list.add(str_1)
        
        return list(final_list)

print(Solution.stringMatching(["mass","as","hero","superhero"]))
        