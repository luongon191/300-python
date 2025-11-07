def nam_nhuan(nam):
    if (nam % 4 == 0 and nam % 100 != 0 or nam % 400 == 0 ):
        return True
    else:
        return False  

try:
    nam = int(input("nhập năm:"))
    if nam_nhuan(nam):
        print("năm nhuận")
    else:
        print("năm ko nhuận")
except ValueError:
    print("Vui lòng nhập lại 1 số mới")