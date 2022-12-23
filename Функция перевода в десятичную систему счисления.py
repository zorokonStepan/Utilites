def conv_to_dec_not(num: str, val: int):
    num = str(num)
    result = int()
    if num.isdigit():
        num1 = int(num)
        i = 0
        while num1 != 0:
            result += (num1 % 10) * val ** i
            i += 1
            num1 //= 10

    else:
        lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
        for j in range(len(num)):
            if num[len(num) - 1 - j] in lst:
                ind = lst.index(num[len(num) - 1 - j])
                result += (ind + 10) * val ** j
            else:
                result += int(num[len(num) - 1 - j]) * val ** j

    return result

print(f'число 111111(2) = {conv_to_dec_not("111111", 2)}(10)')

'''Переведите шестнадцатеричное число 1AF2 в десятичную систему счисления.'''

print(f'число 1AF2(16) = {conv_to_dec_not("1AF2", 16)}(10)')

