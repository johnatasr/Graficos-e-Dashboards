import pandas as pd
import xlrd


# df = pd.read_csv('salaries.csv')
# mat = np.arange(0,50).reshape(5,10)
# df = pd.DataFrame(data=mat)
#
# print(df)

tabela = pd.read_excel("Inventario Rede Inova.xlsx")
df = pd.DataFrame(data=tabela)

print(df)
