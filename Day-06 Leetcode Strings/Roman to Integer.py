def RomanToInt(s):
    '''d={'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
       'IV': 4, 'IX':9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    if len(s)==1:
        return d[s[0]] 
    i=0
    t=0
    le=len(s)-1
    g=[]
    while i<le:
        if s[i] in d:
            if s[i]+s[i+1] in d:
                t=t+d[s[i]+s[i+1]]
                i=i+1
                g.append(s[i])
            else:
                t=t+d[s[i]]
                g.append(s[i])
        i=i+1
    if s[-1]==g[-1]:
        return t
    else:
        t=t+d[s[-1]]
        return t'''
    
    romandeclare = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

    romantonum = []

    for sub_string in s:

        romantonum.append(romandeclare[sub_string])
    
    for i in range(len(s)-1):

        if romantonum[i] < romantonum[i+1]:

            romantonum[i] = -romantonum[i]
        
    return sum(romantonum)
    

print(RomanToInt('MCMXCIV'))
