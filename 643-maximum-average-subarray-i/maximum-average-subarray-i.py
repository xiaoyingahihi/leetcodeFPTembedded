class Solution(object):
    def findMaxAverage(self, nums, k):
        tong_k = sum(nums[:k])
        tong = tong_k
        dodai = len(nums)
        for i in range(k, dodai):
            tong_k += nums[i]
            tong_k -= nums[i-k]
            tong = max(tong, tong_k)
        return tong/float(k)
        