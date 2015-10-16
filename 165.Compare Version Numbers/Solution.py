# __author__ = 'Simon'
# class Solution(object):
#     def compareVersion(self, version1, version2):
#         """
#         :type version1: str
#         :type version2: str
#         :rtype: int
#         """
#         if version1.find('.') != -1 and version2.find('.') != -1:
#             print "AAA"
#             list1 = version1.split('.')
#             list2 = version2.split('.')
#
#             if int(list1[0]) == int(list2[0]) and int(list1[1]) == int(list2[1]):
#                 return 0
#             else:
#                 if (int(list1[0]) > int(list2[0])) or (int(list1[0]) == int(list2[0]) and int(list1[1]) > int(list2[1])):
#                     return 1
#                 else:
#                     return -1
#         else:
#             if version1.find('.') != -1:
#                 list1 = version1.split('.')
#                 if int(list1[0]) >= int(version2):
#                     if int(list1[0]) == int(version2) and int(list1[1]) == 0:
#                         return 0
#                     else:
#                         return 1
#                 else:
#                     return -1
#             if version2.find('.') != -1:
#                 list2 = version2.split('.')
#                 if int(list2[0]) >= int(version1):
#                     if int(list2[0]) == int(version1) and int(list2[1]) == 0:
#                         return 0
#                     else:
#                         return -1
#                 else:
#                     return 1
#             else:
#
#                 if int(version1) > int(version2):
#                     return 1
#                 if int(version1) == int(version2):
#                     return 0
#                 if int(version1) < int(version2):
#                     return -1

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = version1.split('.')
        v2 = version2.split('.')

        i, M = 0, max(len(v1), len(v2))

        for i in range(M):
            n1 = int(v1[i]) if i < len(v1) else 0
            n2 = int(v2[i]) if i < len(v2) else 0

            if n1 != n2:
                return 1 if n1 > n2 else -1

        return 0