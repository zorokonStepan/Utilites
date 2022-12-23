
def convert_decimal_to_any(num: int, val: int):
    """
    перевод числа десятичной системы счисления в другую систему счисления от 2 до 36 включительно
    :param num: число
    :param val: система счисления в которую перевод
    :return: число в нужной системе счисления
    """
    if isinstance(num, int) and isinstance(val, int):
        if val == 10:
            return num

        if val < 2:
            return 'there are no such number systems'

        if val > 36:
            return 'sorry, but this function does not convert more than 36 of the number system'

        lst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        result = ''
        num_tmp = num
        while num_tmp >= val:
            res = num_tmp % val
            if res < 10:
                result += str(res)
            else:
                result += lst[res - 10]
            num_tmp //= val

        if num_tmp < 10:
            result += str(num_tmp)
        else:
            result += lst[num_tmp - 10]

        result = result[::-1]
        return result
    return 'number and the rank of the number system must be integer'


if __name__ == "__main__":
    assert convert_decimal_to_any(25, 2) == '11001'
    assert convert_decimal_to_any(513, 2) == '1000000001'
    assert convert_decimal_to_any(125, 8) == '175'
    assert convert_decimal_to_any(428, 16) == '1AC'
    assert convert_decimal_to_any(1000, 16) == '3E8'
    assert convert_decimal_to_any(255, 16) == 'FF'














