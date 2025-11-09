def giai_thua(n):
    if n <= 0:
        print("giai thừa ko xác định")
    tich = 1
    for i in range(1,n+1):
        tich *= i
    print(tich)

giai_thua(3)