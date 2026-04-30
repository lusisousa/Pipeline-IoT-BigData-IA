import pandas as pd
from sqlalchemy import create_engine, text

# conexão com PostgreSQL
engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/iot_db")

# caminho do CSV
csv_path = "data/temperature_readings.csv"

# ler CSV
df = pd.read_csv(csv_path)

print("Colunas encontradas no CSV:")
print(df.columns)

# renomear colunas para nomes mais fáceis
df = df.rename(columns={
    "room_id/id": "device_id",
    "noted_date": "timestamp",
    "temp": "temperature",
    "out/in": "location_type"
})

print("\nColunas após renomeação:")
print(df.columns)

# converter data
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

# enviar para PostgreSQL
df.to_sql("temperature_readings", engine, if_exists="replace", index=False)

print("\nDados enviados com sucesso para a tabela temperature_readings.")

# executar views
with open("sql/views.sql", "r", encoding="utf-8") as arquivo:
    sql_commands = arquivo.read()

with engine.connect() as conn:
    for command in sql_commands.split(";"):
        if command.strip():
            conn.execute(text(command))
    conn.commit()

print("Views criadas com sucesso.")