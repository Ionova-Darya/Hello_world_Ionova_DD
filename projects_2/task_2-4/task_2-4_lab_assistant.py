volume = float(input("Введите нужный объем раствора (мл): "))
salt_mass = volume * 0.009

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    file.write("-" * 23 + "\n")
    file.write(f"Общий объем: {volume:.2f} мл\n")
    file.write(f"Масса соли:  {salt_mass:.2f} г\n")
    file.write(f"Объем воды:  {volume:.2f} мл")

print("Рецепт сохранен в файл recipe.txt")
