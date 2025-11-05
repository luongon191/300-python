def find_max_of_three(a,b,c):
    if a > b > c or a > c > b :
        return f"{a} là số lớn nhất"
    elif b > c > a or b > a > c:
        return f"{b} là số lớn nhất"
    else:
        return f"{c} là số lớn nhất"
    
try:
    a = int(input())
    b = int(input())
    c = int(input())
    result = find_max_of_three(a,b,c)
    print(result)
except ValueError:
    print("Vui lòng nhập số nguyên hợp lệ.")