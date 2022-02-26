def Keymaker(k):
    keys = []
    for i in range(k):
        keys.append(0)
    step = 1
    for i in range(k):
        if step == 1:
            for j in range(0,k,step):
                if keys[j] == 0:
                    keys[j] += 1
        elif step == 2:
            for j in range(1,k,step):
                if keys[j] == 1:
                    keys[j] -= 1
        elif step == 3:
            for j in range(2,k,step):
                if keys[j] == 1:
                    keys[j] -= 1
                else:
                    keys[j] += 1
        else:
            for j in range(step-1,k,step):
                if keys[j] == 1:
                    keys[j] -= 1
                else:
                    keys[j] += 1
            
        step += 1
    return ("".join(map(str,keys)))