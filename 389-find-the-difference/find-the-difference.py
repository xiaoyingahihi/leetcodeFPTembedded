class Solution(object):
    def findTheDifference(self, s, t):
        for c in t:
            if t.count(c) != s.count(c):
                return c