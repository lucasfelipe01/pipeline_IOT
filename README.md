Pipeline de Dados IoT para Leituras de Temperatura

Descrição do Projeto

Este projeto implementa um pipeline de dados para processar e armazenar leituras de temperatura de dispositivos IoT em um banco de dados PostgreSQL, utilizando Docker. A solução também inclui um painel interativo criado com Streamlit, que visualiza insights como a média de temperatura por dispositivo, leituras por hora e temperaturas máximas e mínimas por dia.

Pré-requisitos

- Python 3.8+
- Docker
- Conta no GitHub e Kaggle

Configuração do Ambiente

1. Clonar o repositório: `git clone (link unavailable)
2. Criar e ativar um ambiente virtual Python:
    - Linux/Mac: python -m venv venv e source venv/bin/activate
    - Windows: venv\Scripts\activate
3. Instalar as dependências necessárias: pip install pandas psycopg2-binary sqlalchemy streamlit plotly
4. Configurar o banco de dados PostgreSQL com Docker:
    - Iniciar o contêiner PostgreSQL: docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
    - Carregar os dados CSV para o banco de dados: python (link unavailable)
5. Executar o painel Streamlit: streamlit run (link unavailable)

Visualizações SQL

1. Média de Temperatura por Dispositivo

Calcula a temperatura média para cada dispositivo.


CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;


2. Leituras por Hora do Dia

Mostra uma contagem de leituras de temperatura agrupadas por hora.


CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora;


3. Temperaturas Máximas e Mínimas por Dia

Calcula as temperaturas máximas e mínimas para cada dia.


CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(timestamp) as data, MAX(temperature) as temp_max, MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY data;


Capturas de Tela do Dashboard

1. Média de temperatura por dispositivo: [imagem]
2. Leituras por Hora do Dia: [imagem]
3. Temperaturas Máximas e Mínimas por Dia: [imagem]

![Captura de tela 2024-11-03 123323](https://github.com/user-attachments/assets/fdab9ddf-4967-4224-80a3-8330230c8d86)


