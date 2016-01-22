import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if not prerequisites:
            return True
        Adj = {}
        for i in range(numCourses):
            Adj[i] = []
        for edge in prerequisites:
            Adj[edge[1]].append(edge[0])
        V = numCourses*[0]
        for i in range(numCourses):
            if V[i] == 0:
                if not self.DFSvisit(i, Adj, V):
                    return False
        return True

    def DFSvisit(self, u, Adj, V):
        V[u] = 1
        for v in Adj[u]:
            if V[v] == 1:
                return False
            if V[v] == 0:
                if not self.DFSvisit(v, Adj, V):
                    return False
        V[u] = 2
        return True