class Solution:
    def wordSubsets(words1: list[str], words2: list[str]) -> list[str]:
        final_word = []

        search_dict = {}
        for word in words2:
            for letter in word:
                if letter in search_dict:
                    search_dict[letter] = max(search_dict[letter], word.count(letter))
                else:
                    search_dict[letter] = 1

        for word in words1:
            flag = True

            for letter in search_dict:
                search_count = search_dict[letter]
                if letter in word:
                    if word.count(letter) < search_count:
                        flag = False
                        break
                else:
                    flag = False
                    break
            
            if flag:
                final_word.append(word)
        
        return final_word


print(Solution.wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))