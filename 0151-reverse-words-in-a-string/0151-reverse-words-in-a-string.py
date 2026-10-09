class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        s=s.split()

        # s=(s.strip()).split()

        s.reverse()
        return " ".join(s)