class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        li = text.split()
        count = 0
        l=0
        r = len(li)
        while l<r:
            for j in brokenLetters:
                if j in li[l]:
                    break
            else:
                count+=1
            l+=1
        return count

