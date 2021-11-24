#Simple Approach

class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        for j in range(len(a)):
            a[j] =a[j][::-1]
        return " ".join(a)
