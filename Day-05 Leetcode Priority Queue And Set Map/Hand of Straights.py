def IsNStraightHand(hand, w):
    hand=sorted(hand)
    if len(hand)%w==0:
        t=[]
        for i in range(0,len(hand),w):
            t.append(hand[i:i+w])
        print(t)        
    else:
        return False

print(IsNStraightHand([1,2,3,6,2,3,4,7,8],3))
