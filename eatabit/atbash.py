def atbash(txt):
    temptxt = []
    for c in txt:
        if ord(c) in range(97,123):
            c = chr((abs(abs(ord(c)-ord('a'))+1-26))+ord('a'))
            temptxt.append(c)
        elif ord(c) in range(65,91):
            c = chr((abs(abs(ord(c)-ord('A'))+1-26))+ord('A'))
            temptxt.append(c)
        else:
            temptxt.append(c)  
    return ''.join(temptxt)          

print(atbash('Apple!'))