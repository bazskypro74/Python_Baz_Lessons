mon = int(input("Введите номер месяца: "))


def month_to_season(mon):
    if (mon == 12 or 1 <= mon <= 2):
        return "Зима"
    if 3 <= mon <= 5:
        return "Весна"
    if 6 <= mon <= 8:
        return "Лето"
    if 9 <= mon <= 11:
        return "Осень"
    else:
        return "Не верный номер месяца"


print(month_to_season(mon))
