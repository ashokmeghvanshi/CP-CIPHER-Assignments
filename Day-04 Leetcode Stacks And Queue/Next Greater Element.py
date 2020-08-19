def NextGreaterElement(nums1,nums2):

    t=[]
    for i in nums1:
        a=nums2.index(i)
       
        if a==len(nums2)-1:
            t.append(-1)
        else:
            s=0
            for j in range(a+1,len(nums2)):
                if i<nums2[j]:
                    t.append(nums2[j])
                    s=0
                    break
                else:
                    s=s+1
            if s!=0:
                t.append(-1)
            
    return t

print(NextGreaterElement([4,1,2],[1,3,4,2]))
print(NextGreaterElement([2,4],[1,2,3,4]))
print(NextGreaterElement([4,5,2],[1,5,3,4,2,9]))
        
