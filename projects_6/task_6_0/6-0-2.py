import pandas as pd
with open("C:/Users/Даша/Desktop/6_0_2.txt", "w") as f:
  df = pd.read_csv("C:/Users/Даша/Downloads/wild_boars.csv")
  col = list(df.columns)
    for i in col[2:]:
        a =  df[i].mean()
        print(f'Boars average is {a:.2f}\n', file=f)
