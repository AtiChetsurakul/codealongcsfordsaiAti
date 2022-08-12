def is_disarium(n):
    ln = len(str(n))
    tempn = n
    sm = 0
    for i in range(ln,0,-1):
        b = tempn %10
        tempn = int(tempn/10)
        sm += pow(b,i)
    return True if sm == n else False


print(is_disarium(135))