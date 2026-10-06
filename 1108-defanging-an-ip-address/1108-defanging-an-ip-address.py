class Solution(object):
    def defangIPaddr(self, address):
        # return address.replace(".", "[.]")

        #with use of loop
        ans=""
        for i in address:
            if i!=".":
                ans+=i
            else:
                ans+="[.]"

        return ans
        