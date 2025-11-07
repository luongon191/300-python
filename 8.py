def dem_chan_le(numbers):
    chan = 0
    le = 0
    for number in numbers:
        if number % 2 == 0 :
            chan += 1
        else:
            le += 1
    return chan,le

try:
    input_list = input("nhập số:")
    numbers = [int(num) for num in input_list.split()]
    chan_soluong, le_soluong = dem_chan_le(numbers)
    print(f"Số lượng số chẵn: {chan_soluong}")
    print(f"Số lượng số lẻ: {le_soluong}")
except ValueError:
    print("Vui lòng nhập các số nguyên hợp lệ.")