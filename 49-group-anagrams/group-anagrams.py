class Solution(object):
    def groupAnagrams(self, strs):
        array={}
        for key in strs:
            keykey = "".join(sorted(key))
            if keykey not in array:
                array[keykey] = []
            array[keykey].append(key)
        return array.values()
        