class Solution:
    def minOperations(boxes: str) -> list[int]:
        ball_index = []
        for box, ball in enumerate(boxes):
            if ball == '1':
                ball_index.append(box)
        
        moves = []
        for box, ball in enumerate(boxes):
            this_move = 0
            for index in ball_index:
                this_move += abs(box-index)
            moves.append(this_move)
        
        return moves

print(Solution.minOperations("001011"))