class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n <= 1:
            return [0]
        degrees = [0] * n
        graph = {}
        for i in range(0,n):
            graph[i] = []
        for edge in edges:
            degrees[edge[1]] += 1
            degrees[edge[0]] += 1
            graph[edge[1]].append(edge[0])
            graph[edge[0]].append(edge[1])

        queue = []
        ret = []
        for j in range(0,n):
            if degrees[j] == 1:
                queue.append(j)
        while queue:
            temp = []
            ret = queue[:]
            for x in queue:
                for n in graph[x]:
                    degrees[n] -= 1
                    if degrees[n] == 1:
                        temp.append(n)
            queue = temp
        return ret