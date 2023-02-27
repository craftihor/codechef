for _ in range(int(input())):
    a,b,x,y = map(int,input().split())
    if(a>=b):
        print(0)
    elif(x==1 and y==1):
        print(-1)
    else:
        tempA, mul=a, 0
        for i in range(100):
            tempA = tempA * x
            mul+=1
            if(tempA >= b):
                break
        tempB, div = b, 0
        for i in range(100):
            tempB = tempB // y
            div+= 1
            if(a >= tempB):
                break
        print(min(mul, div))
