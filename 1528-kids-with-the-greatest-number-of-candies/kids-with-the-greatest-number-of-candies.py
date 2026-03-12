class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        sokeo = max(candies)
        tong = []
        for c in candies:
            if c + extraCandies >= sokeo:
                tong.append(True)
            else:
                tong.append(False)
        return tong