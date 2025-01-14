class Solution:
    def findThePrefixCommonArray(A: list[int], B: list[int]) -> list[int]:
        common_dict = {}
        output = []

        for i in range(len(A)):
            if A[i] not in common_dict:
                common_dict[A[i]] = 0
            if B[i] not in common_dict:
                common_dict[B[i]] = 0

            expected_commons = (i+1)*2
            actual_commons = len(common_dict)
            count = expected_commons - actual_commons
            output.append(count)
        
        return output

print(Solution.findThePrefixCommonArray([1,3,2,4],[3,1,2,4]))