input_n = 1
n = 0
current_mult = 1
remain = input_n

while remain > 0:
    while current_mult << 1 <= remain:
        current_mult <<= 1
    
    n += 1
    remain = remain - current_mult
    current_mult = 1


print(n)