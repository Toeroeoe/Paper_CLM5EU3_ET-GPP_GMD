import pandas as pd

files = []

df_out = pd.DataFrame()

A = 2
B = 1.5

for filename in files:

    df = pd.read_csv(filename)

    Ewe = df['Ewe'] / A

    I = df['<I>'] + B

    df_out[f'Ewe_{filename}', f'<I>_{filename}'] = [Ewe, I]
    
print(df_out)

df_out.to_csv('out.csv')