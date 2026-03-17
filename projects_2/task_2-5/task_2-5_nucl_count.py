print(f"=== Анализ последовательности ДНК ===\n")

def nucleotide_count():

    sequence = input("Введите последовательность ДНК: ").upper()

    print(f"\nПоследовательность в верхнем регистре: {sequence}")

    a_count = sequence.count("A")
    t_count = sequence.count("T")
    g_count = sequence.count("G")
    c_count = sequence.count("C")
    len_sequence = len(sequence)

    return a_count, t_count, g_count, c_count, len_sequence
a_con = (a_count/len_sequence)*100
t_con = (t_count/len_sequence)*100
g_con = (g_count/len_sequence)*100
c_con = (c_count/len_sequence)*100

print(f"\nПодсчёт нуклеотидов:\nA:\t{result[0]}\nT:\t{result[1]}\nG:\t{result[2]}\nC:\t{result[3]}")
print(f"\nОбщая длина: {result[4]}")
print(f"Процентное содержание каждого нуклеотида:\аденина:\t{a_con:.2f}\nтимина:\t{t_con:.2f}\nгуанина:\t{g_con:.2f}\nцитозина:\t{t_con:.2f}")
