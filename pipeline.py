import pandas as pd
from sqlalchemy import create_engine

# Leitura do CSV
df = pd.read_csv('IOT-temp.csv')

# Verifique as primeiras linhas e as colunas do DataFrame
print(df.head())
print(df.columns)

# Renomear colunas removendo espaços, se necessário
df.columns = df.columns.str.strip()  # Remove espaços em branco

# Converta a coluna 'noted_date' para datetime com o formato correto
df['noted_date'] = pd.to_datetime(df['noted_date'], format='%d-%m-%Y %H:%M', errors='coerce')

# Se necessário, você pode verificar se há valores NaT (not a time)
print(df['noted_date'].isna().sum(), "invalid date entries")

# Conectando ao PostgreSQL
engine = create_engine('postgresql://postgres:sua_senha@localhost:5432/postgres')

# Inserindo os dados no banco de dados
df.to_sql('temperature_readings', engine, if_exists='replace', index=False)
