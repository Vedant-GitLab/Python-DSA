class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # return s.reverse()

        #by slicing:
        # s = s[::-1]  #actually ye work nhi kr rha hai qki syd ye iske reference ko mana kr rha hai pr ye bhi shi method hai
        
        #or by using swapping method
        i=0
        j=len(s)-1

        while i<j:
            temp=s[i]
            s[i]=s[j]
            s[j]=temp

            i+=1
            j-=1