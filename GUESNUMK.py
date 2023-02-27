for testcases in range( int(input()) ):
    n,k = map(int,input().split())
    mod_num=n%3
    m1 = m2 = m3 = n//3
    if mod_num==1:
        m1 = n//3 + 1 
    elif mod_num == 2:
        m1 = n//3 + 1
        m2 = n//3 + 1
    
    if k > m1+m2:
        print(3*(k-m1-m2))
    elif k>m1:
        print(3*(k-m1) -1)
    else:
        print(3*(k)-2)
