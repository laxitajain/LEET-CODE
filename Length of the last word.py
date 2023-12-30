class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        t=""
        if len(s)==1 and " " not in s:
            return 1
        if (len(s)==2 or len(s)==3) and " " in s:
            return (len(s)-s.count(" "))
        if " " not in s:
            return len(s)

        for i in range(len(s)-1,0,-1):
            if s[i]!=" ":
                for j in range(i-1,-1,-1):
                    if s[j]==" ":
                        t=s[j+1:i+1]
                        return len(t)
                if " " not in s[i-1:0:-1]:
                    return len(s[:i+1])    
        return 0
