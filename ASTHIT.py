for _ in range(int(input())):
    n = int(input())
    lst =[]
    for _ in range(n):
        lst.append(map(int,input().split()))
    survuved , r = [],[]
    for i in range(len(lst)):
        di,wi = lst[i]
        if di == 0:
            while r:
                dr,wr = r.pop()
                if wi > wr :
                    wi += wr
                else:
                    if wr > wi:
                        r.append([dr,wr+wi])
                    break
            else:
                survuved.append(i+1)
        else:
            r.append([i+1,wi])
    if r:
        for ii,wi in r:
            survuved.append(ii)
    print(len(survuved))
    if len(survuved) > 0:
        result = ' '.join(str(x) for x in survuved)
        print(result)
