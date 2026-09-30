class Solution:
    def isPalindrome(self, nums: int) -> bool:
        temp = nums
        rev = 0
        while temp > 0:
            r = temp%10
            temp//=10
            rev = (rev*10+r)
        if (rev == nums):
            return True
        else :
            return False