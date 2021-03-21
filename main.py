'''Данная программа позволяет проверить корректность введенного номера ИНН или ОГРН
и вывести соотвествующую ему информацию в случае правильно введенного номера'''
def check_ogrn(ogrn):
    '''Проверка правильности введенного номера ОГРН'''
    return len(ogrn) == 13 and (int(ogrn[:-1]) % 11) % 10 == int(ogrn[-1])


def print_info(ogrn):
    '''Вывод информации о предприятии по его ОГРН'''
    print("Признак отнесения государственного регистрационного номера записи: ", end='')
    ogrn1 = int(ogrn[0])
    if (ogrn1 == 1 or ogrn1 == 5):
        print("ОГРН")
    elif (ogrn1 == 3):
        print("ОГРНИП")
    elif (ogrn1 == 4):
        print("ЕГРИП")
    else:
        print("ЕГРЮЛ")

    ogrn2 = ogrn[1:3]
    print("Две последние цифры года внесения записи: " + ogrn2)

    ogrn3 = ogrn[3:5]
    print("Код субъекта РФ: " + ogrn3)

    ogrn4 = ogrn[5:12]
    print("Номер записи, внесенной в государственный реестр в течение года: " + ogrn4)

    ogrn5 = ogrn[12]
    print("Контрольное число: " + ogrn5)

def inn_ctrl_summ(inn):
    ''' Подсчет контрольной суммы '''
    n1 = [7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    n2 = [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8]
    n_1_summ = 0
    n_2_summ = 0
    for i in range(0, len(n1)):
        n_1_summ += int (inn[i]) * int (n1[i])
    for i in range(0, len(n2)):
        n_2_summ += int (inn[i]) * int (n2[i])
    cntl_summ_n1 = n_1_summ % 11 % 10
    cntl_summ_n2 = n_2_summ % 11 % 10
    return cntl_summ_n1, cntl_summ_n2

def inn_check(inn):
    '''Проверка правильности введенного номера ИНН'''
    cntl_summ_n1, cntl_summ_n2 = inn_ctrl_summ(inn)
    return cntl_summ_n1 == int (inn[-2]) and cntl_summ_n2 == int (inn[-1])

def print_inn(inn):
    '''Вывод информации о предприятии по его ИНН'''
    inn1 = inn[0:2]
    print("Код субъекта РФ: " + inn1)

    inn2 = inn[2:4]
    print("Номер местной налоговой инспекции: " + inn2)

    inn3 = inn[5:10]
    print("Номер налоговой записи налогоплательщика в территориальном разделе: " + inn3)

    inn4 = inn[-1]
    print("Контрольное число 1: " + inn4)

    inn5 = inn[-2]
    print("Контрольное число 2: " + inn5)

def inn_or_ogrn ():
    '''Выбор типа проверки в зависимости от вида цифрового кода'''
    check = input ('Введите тип цифрового кода: ИНН или ОГРН ')
    check.upper()
    if check == 'ИНН':
        print("Введите ИНН: ", end='')
        inn = input()
        inn_ctrl_summ(inn)
        while inn_check(inn) == False:
            print("Введён неверный ИНН, повторите попытку: ", end='')
            inn = input()
        print_inn(inn)
    else:
        print("Введите ОГРН: ", end='')
        ogrn = input()
        while not check_ogrn(ogrn):
            print("Введён неверный ОГРН, повторите попытку: ", end='')
            ogrn = input()
        print_info(ogrn)

inn_or_ogrn ()
