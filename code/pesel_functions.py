import re


def search_in(msg):
    peselNumRegex = re.compile(r"\+?\d{11}")
    mo = peselNumRegex.findall(msg)
    return mo


def pesel_birthday(pesel):
    if len(pesel) != 11:
        return False
    year = 0
    month = 0
    if int(pesel[2]) < 2:
        year = 1900
        month = int(pesel[2:4])
    elif int(pesel[2]) < 4:
        year = 2000
        month = int(pesel[2:4]) - 20
    elif int(pesel[2]) < 6:
        year = 2100
        month = int(pesel[2:4]) - 40
    elif int(pesel[2]) < 8:
        year = 1800
        month = int(pesel[2:4]) - 60
    if month < 10:
        month = f"0{month}"
    birthdate = f"{pesel[4:6]}.{month}.{year+int(pesel[0:2])}"
    if int(month) > 12:
        return False
    if int(pesel[4:6]) > 31:
        return False
    return birthdate


def pesel_gender(pesel):
    if len(pesel) != 11:
        return False
    if int(pesel[9]) % 2 == 0:
        return "Women"
    return "Men"


def is_pesel_real(pesel):
    if len(pesel) != 11:
        return False
    algorithm = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
    suma = 0
    for i in range(10):
        suma += algorithm[i] * int(pesel[i])
    real_last = suma % 10
    if real_last == int(pesel[10]):
        return True
    return False


def pesel_info(pesel):
    birth = pesel_birthday(pesel)
    gender = pesel_gender(pesel)
    isReal = is_pesel_real(pesel)
    return birth, gender, isReal
