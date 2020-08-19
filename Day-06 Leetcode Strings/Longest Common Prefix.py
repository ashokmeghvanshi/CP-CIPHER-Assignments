def LongestCommonPrefix(strs):
    if len(strs)==0 or strs==None:
        return ""
    else:
        #n = os.path.commonprefix(strs)
        #return n

        res = '' 
        prefix = strs[0] 

        for string in strs[1:]:
            while string[:len(prefix)] != prefix:
                prefix = prefix[:len(prefix)-1]
            if not prefix:
                break
        res = prefix
        return res


print(LongestCommonPrefix(["flower","flow","flight"]))
    
    
    
    
