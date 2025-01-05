class Solution:
    def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
        final_letter = ''

        letter_to_number = {
            'a':1,'b':2,'c':3,'d':4,'e':5,
            'f':6,'g':7,'h':8,'i':9,'j':10,
            'k':11,'l':12,'m':13,'n':14,'o':15,
            'p':16,'q':17,'r':18,'s':19,'t':20,
            'u':21,'v':22,'w':23,'x':24,'y':25,'z':26
        }
        all_letters = list(letter_to_number.keys())

        difference_array = [0] * len(s)

        for shift_start, shift_end, case in shifts:
            start_change = 1 if case == 1 else -1
            end_change = 1 if start_change == -1 else -1

            difference_array[shift_start] += start_change
            if shift_end+1 < len(s):
                difference_array[shift_end+1] += end_change 
            
            # print(difference_array)
        
        print(difference_array)
        numberOfShifts = 0
        print("LOOP:\n")
        for index, letter in enumerate(s):
            numberOfShifts += difference_array[index]
            print(numberOfShifts)
            new_letter = (letter_to_number[letter]-1 + numberOfShifts)%26
            final_letter += all_letters[new_letter]

        return final_letter

sol = Solution.shiftingLetters(s='abc', shifts=[[0,1,0],[1,2,1],[0,2,1]])
print("Final Letter:" , sol)