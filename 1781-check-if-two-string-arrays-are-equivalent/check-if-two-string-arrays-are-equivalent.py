class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        s1 = ""
        s2 = ""
        for w in word1:
            s1 += w
        for w in word2:
            s2 += w
        if s1 == s2:
            return True
        else:
            return False