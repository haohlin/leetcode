while True:
    try:
        str_list = input()
        if not str_list:
            break
        min_len = len(str_list)
        i = 0
        while i < len(str_list):
            count = 0
            temp_i = i
            for j in range(i+1, len(str_list)):
                i = j
                if str_list[j] == str_list[i]:
                    count += 1
                else:
                    break
            if count >= 4:
                min_len -= j - temp_i - (len(str(count)) + 3) + 1
            i += 1
        print(min_len)
    except:
        break