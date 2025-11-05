def check_even_odd(n):
    if n % 2 == 0 :
        return "số đó là số chẵn"
    else:
        return "số đó là số lẻ"

try:
    number = int(input("nhập vào một số nguyên: "))
    result = check_even_odd(number)
    print(result)
except ValueError:
    print("Vui lòng nhập một số hợp lệ")  
          