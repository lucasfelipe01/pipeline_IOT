import streamlit as st
import pandas as pd
import pipeline

from sqlalchemy import create_engine

# Configurações de conexão com o PostgreSQL
engine = create_engine('postgresql://postgres:sua_senha@localhost:5432/postgres')

# Título do Dashboard
st.title("Dashboard de Temperaturas IoT")

# Exibir média de temperatura por dispositivo
st.header("Média de Temperatura por Dispositivo")
avg_temp_query = "SELECT \"room_id/id\", AVG(temp) AS avg_temp FROM temperature_readings GROUP BY \"room_id/id\";"
avg_temp_df = pd.read_sql(avg_temp_query, engine)
st.bar_chart(avg_temp_df.set_index("room_id/id"))

# Exibir leituras por hora
st.header("Leituras por Hora")
leituras_query = "SELECT EXTRACT(HOUR FROM noted_date) AS hora, COUNT(*) AS contagem FROM temperature_readings GROUP BY hora;"
leituras_df = pd.read_sql(leituras_query, engine)
st.line_chart(leituras_df.set_index("hora"))

# Exibir temperaturas máximas e mínimas por dia
st.header("Temperaturas Máximas e Mínimas por Dia")
temp_max_min_query = "SELECT DATE(noted_date) AS data, MAX(temp) AS temp_max, MIN(temp) AS temp_min FROM temperature_readings GROUP BY data;"
temp_max_min_df = pd.read_sql(temp_max_min_query, engine)
st.area_chart(temp_max_min_df.set_index("data"))

# Executar o app
if __name__ == "__main__":
    st.write("Dashboard em execução!")
