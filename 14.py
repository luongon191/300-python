def find_number1():
    list_number = []
    count = int(input("số lần nhập:"))
    for i in range(count):
        nhap = int(input(f"nhập lần thứ {i+1}:"))
        list_number.append(nhap)
    list_number.sort(reverse = True)
    print(list_number[1])

find_number1()