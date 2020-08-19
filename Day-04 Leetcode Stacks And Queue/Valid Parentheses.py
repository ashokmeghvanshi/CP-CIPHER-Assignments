
def IsValid(string):
    stack=[]
    for i in string:
        if i in ['(','{','[']: stack.append(i)
        else:
            if not stack:
                return False
            stacktop=stack.pop()
            if stacktop=='(':
                if i!=')':
                    return False
            if stacktop=='{':
                if i!='}':
                    return False
            if stacktop=='[':
                if i!=']':
                    return False
    if len(stack)>0:
        return False
    return True


print(IsValid('{}(){[()]}'))
print(IsValid('{}(()]}'))
