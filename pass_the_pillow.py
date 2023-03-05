class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        direction = 1
        person = 1
        currentIndex = 1
        for i in range(1, time+1):
            currentIndex += 1
            if currentIndex > n: 
                currentIndex = 2
                if direction > 0: direction = -1
                else: direction = 1
            person += direction

        return person
            

n = 18
time = 38
print(Solution().passThePillow(n,time))