import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        ans = ''
        for x in range(len(set(s))):
            top, idx = s[0], 0
            counter = collections.Counter(s)
            for y in range(len(s)):
                if top > s[y]:
                    top, idx = s[y], y
                if counter[s[y]] == 1:
                    break
                counter[s[y]] -= 1
            ans += top
            s = s[idx+1:].replace(top,'')
        return ans



if __name__ == '__main__':
    S = Solution()
    S.removeDuplicateLetters("cbacdcbc")