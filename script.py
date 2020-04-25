import pesel_functions as pf

pesel = []
birthdate = []
gender = []
status = []
line_number = []

path = str(input("Path: "))
input_file = open(path, "r")

lines = input_file.readlines()
nr_line = 0
for line in lines:
    nr_line += 1
    pesel_line = pf.search_in(line)
    if len(pesel_line) > 0:
        line_number.append(nr_line)
        for pes in pesel_line:
            pesel.append(pes)
inputs = len(pesel)

for nr_pesel in range(inputs):
    birth, gend, stat = pf.pesel_info(pesel[nr_pesel])
    birthdate.append(birth)
    gender.append(gend)
    status.append(stat)

real = 0
fake = 0

for nr_pesel in range(inputs):
    if (
            status[nr_pesel] is True
            and birthdate[nr_pesel] is not False
            and gender[nr_pesel] is not False
    ):
        real += 1
    else:
        fake += 1

if real > 1:
    print(f"In {path} there are {real} Pesel numbers: ")
    print()
elif real == 1:
    print(f"In {path} there is only {real} Pesel numbers: ")
    print()
else:
    print(f"No Pesel numbers in {path}")
    exit()

for nr_pesel in range(inputs):
    if (
            status[nr_pesel] is True
            and birthdate[nr_pesel] is not False
            and gender[nr_pesel] is not False
    ):
        print(f"Pesel: {pesel[nr_pesel]}")
        print(f"In line {line_number[nr_pesel]}")
        print(f"Date of birth: {birthdate[nr_pesel]}")
        print(f"Gender: {gender[nr_pesel]}")
        print()

if fake > 1:
    print(
        f"In {path} there are {fake} numbers that are not Pesel numbers but are similar"
    )
    print()
elif fake == 1:
    print(
        f"In {path} there is {fake} number that is not a Pesel number but it is similar"
    )
    print()
else:
    exit()

answer = str(input("Do you want to see it? [Y/n]: "))
answer.lower()
if answer == "y":
    for nr_pesel in range(inputs):
        if status[nr_pesel] is False or birthdate[nr_pesel] is False:
            print(f"Pesel: {pesel[nr_pesel]}")
            print(f"In line {line_number[nr_pesel]}")
            print()
else:
    exit()
