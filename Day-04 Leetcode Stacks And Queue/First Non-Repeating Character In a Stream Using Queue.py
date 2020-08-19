from queue import Queue

def FirstNonRepeatingCharacter(Str):
    q=Queue()
    alpha={'a': 0, 'b': 0, 'c': 0,'d': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0,
           'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0,
           't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    
    for i in range(len(Str)):

        q.put(Str[i])

        alpha[Str[i]]=alpha[Str[i]]+1

        while (not q.empty()):

            if alpha[q.queue[0]]>1:
                q.get()

            else:
                print(q.queue[0],end=' ')
                break

        if q.empty():
            print(-1,end=' ')
        
    print()    

Str=('aqizqazpn')

FirstNonRepeatingCharacter(Str)
