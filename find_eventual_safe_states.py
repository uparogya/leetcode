class Solution:
    def eventualSafeNodes(graph: list[list[int]]) -> list[int]:
        lengths_dict = {}
        safe_nodes = set()
        iterated = set()

        for index, node in enumerate(graph):
            if len(node) == 0:
                safe_nodes.add(index)
            else:
                if len(node) in lengths_dict:
                    lengths_dict[len(node)].append(index)
                else:
                    lengths_dict[len(node)] = [index]

        while len(safe_nodes) not in iterated:
            iterated.add(len(safe_nodes))

            for i in range(1,len(safe_nodes)+1):
                if i not in lengths_dict:
                    continue

                for prev_index in lengths_dict[i]:
                    # print(prev_index)
                    flag = True
                    for element in graph[prev_index]:
                        if element not in safe_nodes:
                            flag = False
                            break
                    if flag:
                        safe_nodes.add(prev_index)
        
        return (sorted(list(safe_nodes)))

print(Solution.eventualSafeNodes([[],[0,2,3,4],[3],[4],[]]))