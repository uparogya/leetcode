class Solution:
    def highestPeak(isWater: list[list[int]]) -> list[list[int]]:
        peaks = isWater.copy()
        m = len(isWater)
        n = len(isWater[0])
        
        def returnAdjacent(vertex):
            x_change = [-1,0,0,1]
            y_change = [0,-1,1,0]
            adjacent_vertices = []
            for i in range(4):
                this_vertex = (vertex[0]+x_change[i],vertex[1]+y_change[i])
                if this_vertex[0] < 0 or this_vertex[1] < 0 or this_vertex[0] >= m or this_vertex[1] >= n:
                    continue
                else:
                    adjacent_vertices.append(this_vertex)
            
            return adjacent_vertices
        
        vertex_stack = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    peaks[i][j] = 0
                    vertex_stack.append(((i,j),0))
                else:
                    peaks[i][j] = None

        while vertex_stack:
            this_set = vertex_stack.pop(0)
            current_vertex = this_set[0]
            peak_value = this_set[1] + 1

            adjacent_vertices = returnAdjacent(current_vertex)
            for vertex in adjacent_vertices:
                if peaks[vertex[0]][vertex[1]] == None:
                    peaks[vertex[0]][vertex[1]] = peak_value
                    vertex_stack.append(((vertex[0],vertex[1]),peak_value))
        
        return peaks

print(Solution.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))