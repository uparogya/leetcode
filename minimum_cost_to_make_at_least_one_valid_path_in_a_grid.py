import heapq

class Solution:
    def minCost(grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def immediateNext(coordinate):
            sign = grid[coordinate[0]][coordinate[1]]
            if sign == 1:
                return(coordinate[0],coordinate[1]+1)
            elif sign == 2:
                return(coordinate[0],coordinate[1]-1)
            elif sign == 3:
                return(coordinate[0]+1,coordinate[1])
            else:
                return(coordinate[0]-1,coordinate[1])

        def validNext(coordinate, current_cost):
            immediate_next = immediateNext(coordinate)
            temp_coordinates = [(coordinate[0],coordinate[1]+1), (coordinate[0],coordinate[1]-1), (coordinate[0]+1,coordinate[1]), (coordinate[0]-1,coordinate[1])]
            next_coordinates = []
            for coors in temp_coordinates:
                if coors[0] < 0 or coors[0] > m-1 or coors[1] < 0 or coors[1] > n-1:
                    continue
                
                if coors == immediate_next:
                    weight = 0
                else:
                    weight = 1
                
                heapq.heappush(next_coordinates, (current_cost+weight, coors))

            return next_coordinates

        visited = set()

        minCost = [[99999999 for _ in range(n)] for _ in range(m)]
        minCost[0][0] = 0

        def findPath():
            fringe = []
            
            visited.add((0,0))
            fringe.append((0, (0,0)))

            while fringe:
                current = heapq.heappop(fringe)
                next_coors = validNext(current[1], current[0])
                
                visited.add(current[1])

                if current[1] == (m-1,n-1):
                    return

                print('MC:',current[1])

                for coors in next_coors:
                    coor = coors[1]
                    weight = coors[0]
                    if coor in visited:
                        continue
                    
                    next_cost = weight
                    print(coor)
                    if next_cost < minCost[coor[0]][coor[1]]:
                        minCost[coor[0]][coor[1]] = next_cost
                        heapq.heappush(fringe,(next_cost, coor))
                    
                    # if coor == (m-1,n-1):
                    #     return

                    # visited.add(coor)
        
        findPath()
        # print(validNext((0,2),0))
        return minCost[m-1][n-1]

print(Solution.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))