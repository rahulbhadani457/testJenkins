class Solution:
    def searchInsert(self, nums: list[int], target: int, left: int, right: int) -> int:
        if (left-right) == 0:
            return False
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        
        if nums[mid] > target:
            return self.searchInsert(nums, target, 0, mid)
        else:
            return self.searchInsert(nums, target, mid, right)
        

if __name__ == "__main__":
    a = Solution()
    arr = [1,2,3,4,5]
    print(a.searchInsert(arr, 4,0,len(arr)))
kgugiuhhlk