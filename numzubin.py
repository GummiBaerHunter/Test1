def bin_to_dec(decimal_num):
    if decimal_num == 0:
        return "0"
    
    negative = decimal_num < 0
    decimal_num = abs(decimal_num)
    
    binary_num = ""
    while decimal_num > 0:
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num //= 2
        
    return "-" + binary_num if negative else binary_num

print(bin_to_dec(int(input("bitte_gib_mir_eine_zahl:"))))


