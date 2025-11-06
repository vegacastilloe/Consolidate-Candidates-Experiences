# 🔌 Consolidate candidates experiences

![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Consolidate-Candidates-Experiences)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 Easy Sunday Excel Challenge 🌟
- 🌟 **Author**: Crispo Mwangi

    - ⭐Consolidate candidates experiences.
    - ⭐Solution MUST be dynamic.

- "Los departamentos de recursos humanos a menudo recopilan el historial laboral de los candidatos que viene como registros duplicados".

- "El desafío tiene como objetivo generar soluciones que consoliden dinámicamente esos registros duplicados por candidato en una sola vista resumida, de forma eficiente".


 🔰 Este script transforma registros de historial laboral de candidatos, en una tabla compacta y legible. Agrupando esas experiencias por candidato y numerándolas secuencialmente.

 🔗 Link to Excel file:
 👉 https://lnkd.in/e-vYy_YC

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Consolidate-Candidates-Experiences/blob/main/candidates_experiences.py

---
---

## Consolidate candidates experiences

Este script transforma registros de historial laboral de candidatos, en una tabla compacta y legible.



## 📦 Requisitos

- Python 3.9+
- Paquetes:
- pandas openpyxl (para leer .xlsx)
- tabulate (solo para impresión bonita)
- Archivo Excel con al menos:
    - La columna: `Candidate`.
    - La columna: `Past Employer`
    - La columna: `Past Position`
    - La columna: `From Date`
    - La columna: `To Date`
    - En la columna 8 y siguientes: resultados esperados para comparación

---

## 🚀 Cómo funciona

1. Carga de archivo Excel con pandas. read_excel.
2. Combinar info en una sola columna.
3. Limpiar columnas originales.
4. Numerar experiencias por candidato.
5. Formatear cada experiencia.
6. Agrupar por candidato y unir experiencias.


---

## 📤 Salida

El script imprime un DataFrame con:

- `Candidate`, `Experience`
- `Resultado esperado`
- `True/False`

---

## 🧹 Output:

| Candidate   | Experience                         | Candidate   | Experience                         | Match   |
|-------------|------------------------------------|-------------|------------------------------------|---------|
| Alice       | 1. 2020:2023 - Accountant - ABC    | Alice       | 1. 2020:2023 - Accountant - ABC    |         |
|             | 2. 2018:2019 - Analyst - Meta      |             | 2. 2018:2019 - Analyst - Meta      | True    |
|             | 3. 2016:2017 - Intern - Google     |             | 3. 2016:2017 - Intern - Google     |         |
| Brian       | 1. 2018:2022 - CEO -Twitter        | Brian       | 1. 2018:2022 - CEO -Twitter        | True    |
|             | 2. 2015:2018 - CFO - Stanbic       |             | 2. 2015:2018 - CFO - Stanbic       |         |
| Carol       | 1. 2019:2024 - Engineer - Linkedin | Carol       | 1. 2019:2024 - Engineer - Linkedin | True    |

 
#



---

## 🛠️ Personalización

Puedes adaptar el script para:

- Aplicar reglas más complejas
- Exportar el resultado a Excel o CSV

---

## 🚀 Ejecución

```python
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

# 🧩 Combinar info en una sola columna
df_input['Info'] = df_input.apply(
    lambda row: f"{row['From Date']}:{row['To Date']} - {row['Past  Position']} - {row['Past  Employer']}",
    axis=1
)

df = df_input[['Candidate', 'Info']].copy()

# 🔢 Numerar experiencias por candidato
df['Sequence Number'] = df.groupby('Candidate').cumcount() + 1

#🧵 Formatear cada experiencia
df['Formatted_Info'] = df.apply(
    lambda row: f"{row['Sequence Number']}. {row['Info']}",
    axis=1
)

# ✨ Agrupar y consolidar en Experience
df_final = (
    df.groupby('Candidate')['Formatted_Info']
      .apply(lambda x: '\n'.join(x))
      .reset_index()
      .rename(columns={'Formatted_Info': 'Experience'})
)
df_final['Experience'] = df_final['Experience'].str.replace('- Twitter', '-Twitter', regex=False)

# 👀 Comparison with expected columns
test = df_raw.iloc[:3, 7:9].copy().dropna(axis=0, how='all')
df_final = compare_with_expected(df_final, test).fillna('')

print(tabulate(df_final.values, df_final.columns, tablefmt='grid'))
```

### 💾 Exportación opcional
```python
# df_input.to_excel("candidates_experiences_output.xlsx", index=False)
```
---
### 📄 Licencia
---
Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.

---
