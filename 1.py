def check_number(n):
    if n > 0:
        return "Số bạn nhập là số dương."
    elif n < 0:
        return "Số bạn nhập là số âm."
    else:
        return "Số bạn nhập là số không (không phải dương cũng không phải âm)."


try:
    number = int(input("Nhập một số nguyên: "))
    result = check_number(number)
    print(result)
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")    
    