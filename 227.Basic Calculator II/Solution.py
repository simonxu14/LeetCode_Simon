class Solution(object):
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         list = []
#         i = 0
#         while i < len(s):
#             if s[i].isspace():
#                 i += 1
#                 continue
#             elif s[i].isdigit():
#                 temp = i
#                 while i+1<len(s) and s[i+1].isdigit():
#                     i += 1
#                 list.append(s[temp:i+1])
#             else:
#                 list.append(s[i])
#             i += 1
#         print list
#
#         j = 0
#         while j < len(list):
#             if list[j] == "*":
#                 list[j-1] = int(list[j-1])*int(list[j+1])
#                 del list[j]
#                 del list[j]
#                 j -= 1
#                 if len(list) == 1:
#                     break
#             elif list[j] == "/":
#                 list[j-1] = int(list[j-1])/int(list[j+1])
#                 del list[j]
#                 del list[j]
#                 j -= 1
#                 if len(list) == 1:
#                     break
#             j += 1
#
#         k = 0
#         while k < len(list):
#             if list[k] == "+":
#                 list[k-1] = int(list[k-1])+int(list[k+1])
#                 del list[k]
#                 del list[k]
#                 k -= 1
#                 if len(list) == 1:
#                     break
#             elif list[k] == "-":
#                 list[k-1] = int(list[k-1])-int(list[k+1])
#                 del list[k]
#                 del list[k]
#                 k -= 1
#                 if len(list) == 1:
#                     break
#             k += 1
#
#         return list[0]

    def calculate(self, s):
        s += '+'
        result = 0
        temp = 0
        number, operation = '', '+'
        for c in s:
            if c == ' ':
                pass
            elif c.isdigit():
                number += c
            else:
                if operation in '+-':
                    result += temp
                    val = int(number)
                    if operation == '-':
                        val = -val
                    temp = val
                elif operation == '*':
                    temp *= int(number)
                elif operation == '/':
                    if temp < 0:
                        temp /= -int(number)
                        temp = -temp
                    else:
                        temp /= int(number)
                number = ''
                operation = c
        return result + temp








if __name__ == '__main__':
    s = Solution()
    print s.calculate("1")