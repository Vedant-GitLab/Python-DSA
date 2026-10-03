class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        #it is same as question no. 26 but here we have to ignore the third same occurance of digit 
        n = len(nums)
        if n<= 2:
            return n

        start = 1
        for i in range(2, n):
            if nums[i]!=nums[start-1]:
                start += 1
                nums[start] = nums[i]

        return start+1
        