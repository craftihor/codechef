def fun(x):
    while True:
        x = x + 1
        y = str(x)
        for i in y:
            flag = True
            if y.count(i) > 1:
                flag = False
                break
        if flag:
            print(x)
            break
        else:
            pass
                
 
t = int(input())

while t > 0:
    x = int(input())
    fun(x)
    t = t-1
