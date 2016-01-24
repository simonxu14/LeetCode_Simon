# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return
        root = UndirectedGraphNode(node.label)
        stack = [node]
        visit = {}
        visit[node.label] = root
        while stack:
            top = stack.pop()
            for n in top.neighbors:
                if n.label not in visit:
                    stack.append(n)
                    visit[n.label] = UndirectedGraphNode(n.label)
                visit[top.label].neighbors.append(visit[n.label])
        return root

        # if not node:
        #     return
        # root = UndirectedGraphNode(node.label)
        # stack = [node]
        # visit = []
        # visit.append(node)
        # while stack:
        #     top = stack.pop()
        #     for n in top.neighbors:
        #         temp = 0
        #         for k in visit:
        #             if n.label == k.label:
        #                 top.neighbors.append(k)
        #                 break
        #             else:
        #                 temp += 1
        #         if temp == len(visit):
        #             stack.append(n)
        #             new = UndirectedGraphNode(n.label)
        #             visit.append(new)
        #             top.neighbors.append(new)
        # return root