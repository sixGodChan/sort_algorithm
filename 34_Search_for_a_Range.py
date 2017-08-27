class Solution(object):
    def searchRange(self, nums, target):
        high = len(nums) - 1
        low = 0
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                a = mid
                b = mid
                while a >= 0 and nums[a] == target:
                    a -= 1
                while b < len(nums) and nums[b] == target:
                    b += 1
                return [a+1, b-1]
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return [-1, -1]


s = Solution()
o = s.searchRange([1, 2, 3, 4, 5, 5, 5, 6], 6)
print(o)
