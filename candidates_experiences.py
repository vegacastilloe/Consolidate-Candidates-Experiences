import pandas as pd
from tabulate import tabulate

# 🧩 Datos originales
df_raw = pd.read_excel(xl, header=2)

# 🎯 Seleccionar columnas útiles
df_input = df_raw.iloc[:6, 1:6].dropna(axis=0, how='all')
df_input[['From Date', 'To Date']] = df_input[['From Date', 'To Date']].astype(float).astype('Int64').astype(str)

# 🧠 Comparison function
def compare_with_expected(df_actual, df_expected_raw):
    df_expected = df_expected_raw.dropna(how='all').rename(columns=lambda x: x.replace('.1', '')).fillna('')
    comparison = df_actual.eq(df_expected.reset_index(drop=True)).all(axis=1)
    return pd.concat([df_actual, df_expected, comparison.rename('Match')], axis=1)

df_input['Info'] = df_input.apply(
    lambda row: f"{row['From Date']}:{row['To Date']} - {row['Past  Position']} - {row['Past  Employer']}",
    axis=1
)

df = df_input[['Candidate', 'Info']].copy()

df['Sequence Number'] = df.groupby('Candidate').cumcount() + 1

df['Formatted_Info'] = df.apply(
    lambda row: f"{row['Sequence Number']}. {row['Info']}",
    axis=1
)

# Agrupar y consolidar en Experience
df_final = (
    df.groupby('Candidate')['Formatted_Info']
      .apply(lambda x: '\n'.join(x))
      .reset_index()
      .rename(columns={'Formatted_Info': 'Experience'})
)
df_final['Experience'] = df_final['Experience'].str.replace('- Twitter', '-Twitter', regex=False)

# Comparison with expected columns
test = df_raw.iloc[:3, 7:9].copy().dropna(axis=0, how='all')
df_final = compare_with_expected(df_final, test).fillna('')

print(tabulate(df_final.values, df_final.columns, tablefmt='grid'))

# 💾 Exportación opcional
# df_input.to_excel("candidates_experiences_output.xlsx", index=False)