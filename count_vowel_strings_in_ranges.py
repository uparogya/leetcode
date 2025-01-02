class Solution:
    def vowelStrings(words: list[str], queries: list[list[int]]) -> list[int]:
        output = []
        vowels = ('a','e','i','o','u')
        temp_sums = []
        
        current_outer_sum = 0
        for word in words:
            if word[0] not in vowels or word[len(word)-1] not in vowels:
                current_outer_sum += 0
            else:
                current_outer_sum += 1

            temp_sums.append(current_outer_sum)

        # print(temp_sums)
        
        for query in queries:
            if query[0] > 0:
                output.append(temp_sums[query[1]]-temp_sums[query[0]-1])
            else:
                output.append(temp_sums[query[1]])
        
        return (output)
    
words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
print(Solution.vowelStrings(words=words,queries=queries))