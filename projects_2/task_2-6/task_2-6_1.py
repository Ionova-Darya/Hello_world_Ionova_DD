def ph_indetificator(ph_value):
    if ph_value > 7:
        return "Основная среда"
    elif ph_value < 7:
        return "Кислая среда"
    else:
        return "Нейтральная среда"

result = ph_indetificator(float(input("Введите значение pH: ")))
print(result)
