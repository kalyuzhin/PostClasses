import string

CLASSES = {'P0': "",
           'P1': "",
           'L': "",
           'S': "",
           'M': ""}


def convert_to_binary(number: int, vars: int):
    result = ''
    while number > 0:
        result += str(number % 2)
        number //= 2
    while len(result) != vars:
        result += str(0)
    return result[::-1]


def first_class(eval: str):
    """Сохранение 0"""
    if (int(eval[0])):
        CLASSES['P0'] = '-'
    else:
        CLASSES['P0'] = '+'


def second_class(eval: str):
    """Сохранение 1"""
    if int(eval[-1]):
        CLASSES['P1'] = '+'
    else:
        CLASSES['P1'] = '-'


def third_class(eval: str, m: int):
    """ Линейность """
    a0 = int(eval[0])
    a = []
    shift = 1
    elem = 1
    count = 0

    while count < m:
        a.append(int(eval[elem]) ^ a0)
        elem += shift
        shift *= 2
        count += 1
    current_s = [[a0 ^ (a[0] * x) for x in range(2)]]
    c = 2
    for i in range(1, len(a)):
        current_s.append([current_s[i - 1][x] ^ (a[i] * y) for y in range(2) for x in range(c)])
        c *= 2
        # print(current_s)
    result = ''.join(str(current_s[-1][i]) for i in range(2 ** m))
    # print(result)
    # print(a)
    if result == eval:
        CLASSES['L'] = '+'
    else:
        CLASSES['L'] = '-'


def fourth_class(eval: str, m: int):
    """ Самодвойственность """
    var = 2 ** m
    new_eval = ''
    for x in reversed(eval):
        new_eval += (str(int(not (int(x)))))
    flag = True
    for i in range(var):
        if eval[i] != new_eval[i]:
            flag = False
            break
    if flag:
        CLASSES['S'] = '+'
    else:
        CLASSES['S'] = '-'


def fifth_class(eval: str, m: int):
    """ Монотонность """
    a = []
    for i in range(len(eval)):
        bin_number = convert_to_binary(i, m)
        a.append(bin_number)
    flag = True
    for i in range(len(eval)):
        if eval[i] == '1':
            for j in range(i + 1, len(eval)):
                if all(a[j][k] >= a[i][k] for k in range(m)) and eval[j] < eval[i]:
                    flag = False
                    break
    if flag:
        CLASSES['M'] = '+'
    else:
        CLASSES['M'] = '-'


def task1(m: int, eval: str):
    """ Результирующая функция """

    var = 2 ** m
    assert (len(eval) == var)
    assert (all(f in string.digits for f in eval))
    first_class(eval)
    second_class(eval)
    third_class(eval, m)
    fourth_class(eval, m)
    fifth_class(eval, m)


def main():
    m = int(input("Введите количество переменных: "))
    eval = input("Введите eval: ")
    task1(m, eval)
    print(CLASSES)


if __name__ == '__main__':
    main()
