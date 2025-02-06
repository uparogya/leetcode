from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        requirements = defaultdict(list)
        indegree = [0] * numCourses

        for requisite in prerequisites:
            requirements[requisite[0]].append(requisite[1])
            indegree[requisite[1]] += 1

        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        nodePrerequisites = defaultdict(set)

        while q:
            node = q.popleft()

            for requirement in requirements[node]:
                nodePrerequisites[requirement].add(node)

                for prereq in nodePrerequisites[node]:
                    nodePrerequisites[requirement].add(prereq)

                indegree[requirement] -= 1
                if indegree[requirement] == 0:
                    q.append(requirement)
        
        output = []
        for q in queries:
            output.append(q[0] in nodePrerequisites[q[1]])
        
        return output

        # have to learn Kahn's Algorithm
        
        
print(Solution().checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))