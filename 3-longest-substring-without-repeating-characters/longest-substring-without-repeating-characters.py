class Solution(object):
    def lengthOfLongestSubstring(self, s):
        kytu = set(); left = 0; dodai = 0
        for right in range(len(s)):
            while s[right] in kytu:
                kytu.remove(s[left])
                left += 1
            kytu.add(s[right])
            dodai = max(dodai, right - left +1)
        return dodai
        