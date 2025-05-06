def is_year_leap(year):
    return "True" if year % 4 == 0 else "False"


god = int(input("Введите значение года: "))
result = is_year_leap(god)
print(f"год {god}: {result}")
