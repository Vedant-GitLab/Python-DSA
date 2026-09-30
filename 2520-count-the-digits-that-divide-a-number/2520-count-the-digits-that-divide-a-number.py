class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        sum = 0
        while temp>0:
            r = temp%10
            if num%r==0:
                sum+=1
            temp//=10

        return sum    