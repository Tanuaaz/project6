def check_ogrn(ogrn):
    '''Проверка правильности введенного номера'''
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


print("Введите ОГРН: ", end='')
ogrn = input()
while not check_ogrn(ogrn):
    print("Введён неверный ОГРН, повторите попытку: ", end='')
    ogrn = input()
print_info(ogrn)
