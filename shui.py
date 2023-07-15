def fun1(y):
    bit = y%100%10
    ten = y%100//10
    hud = y//100
    m = bit**3 + ten**3 + hud**3
    if m == y :
        print("是水仙花数")
    else :
        print("不是水仙花数")

def fun2(x):
    z= 0
    for i in range(1,x+1):
        if x % i == 0:
            z = z + 1
    if z > 2:
        print("不是素数")
    else :
        print("是素数")       