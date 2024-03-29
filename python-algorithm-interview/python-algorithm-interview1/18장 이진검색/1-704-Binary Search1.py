class Solution:
    def search(self, nums, target):
        def binary_search(left, right):
            if left < right:
                mid = (left + right) // 2
                
                if nums[mid] < target:
                    return binary_search(mid+1, right)
                elif nums[mid] > target:
                    return binary_search(left, right-1)
                else:
                    return mid
                
            else:
                return -1
        return binary_search(0, len(nums) - 1)