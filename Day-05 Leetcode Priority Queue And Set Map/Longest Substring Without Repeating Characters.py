def LengthOfLongestSubstring(s):
    
    l=0
    j=0
    t=0
    d=''
    while(j<len(s)):
        i=j
        while(i<len(s)):
            if s[i] not in d:
                d=d+s[i]
                l=l+1
                if l>t:
                    t=l
            else:
                d=''
                l=0
                j=j+1
                break
            i=i+1
    return t    
print(LengthOfLongestSubstring('aab'))
