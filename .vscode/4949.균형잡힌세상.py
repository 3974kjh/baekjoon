while (1):
    stack = input()
    res = []    
    out = 'yes'
    if (stack == '.'):
        break
    for i in range(len(stack)):
        if (stack[i] == '('):
            res.append(1)
        elif (stack[i] == '['):
            res.append(2)
        elif (stack[i] == ']' or stack[i] == ')'):
            if (len(res) == 0):
                out = 'no'
                break
            elif (res[len(res)-1] == 1 and stack[i] == ')'):
                if (len(res) != 0):
                    res.pop()
                else:
                    out = 'no'
                    break
            elif (res[len(res)-1] == 2 and stack[i] == ']'):
                if (len(res) != 0):
                    res.pop()
                else:
                    out = 'no'
                    break
            else:
                out = 'no'
                break
    if (len(res) > 0):
        out = 'no'
    print(out)