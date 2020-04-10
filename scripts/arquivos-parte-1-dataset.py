# Maninpulando arquivos com Pandas
import pandas as pd
versao = pd.__version__

file_name = "arquivos/salarios.csv"
df = pd.read_csv(file_name)
print(df.head())