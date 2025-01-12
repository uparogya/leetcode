class Solution:
    def canBeValid(s: str, locked: str) -> bool:

        # first edge case: starts with locked ) or ends with locked (
        if (s[0] == ')' and locked[0] == '1') or (s[len(s)-1] == '(' and locked[len(s)-1] == '1') or len(s)%2 != 0:
            return False

        bracket_stack = []
        unlocked_count = []
        for index, char in enumerate(s):
            if locked[index] == '0':
                # if len(bracket_stack) > 0:
                #     bracket_stack.pop()
                # else:
                unlocked_count.append(index)
            else:
                if char == '(':
                    bracket_stack.append(index)
                if char == ')':
                    if len(bracket_stack) > 0:
                        bracket_stack.pop()
                    elif len(unlocked_count) > 0:
                        unlocked_count.pop()
                    else:
                        return False
        
        print(bracket_stack)
        print(unlocked_count)

        while unlocked_count and bracket_stack and bracket_stack[-1] < unlocked_count[-1]:
            unlocked_count.pop()
            bracket_stack.pop()
        
        if bracket_stack:
            return False
        
        return True

print(Solution.canBeValid("())()))()(()(((())(()()))))((((()())(())","1011101100010001001011000000110010100101"))


        