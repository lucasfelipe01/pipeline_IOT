# Pipeline de Dados IoT para Leituras de Temperatura

## Descrição do Projeto
Este projeto implementa um pipeline de dados para processar e armazenar leituras de temperatura de dispositivos IoT em um banco de dados PostgreSQL, utilizando Docker. A solução inclui um painel interativo criado com Streamlit, que visualiza insights como a média de temperatura por dispositivo, leituras por hora e temperaturas máximas e mínimas por dia.

O fluxo de trabalho do projeto envolve:

- Processar um arquivo CSV (IOT-temp.csv) com leituras de temperatura de dispositivos IoT.
- Armazenar os dados em um banco de dados PostgreSQL usando SQLAlchemy.
- Criar visualizações dinâmicas dos dados via Streamlit.

## Como configurar o ambiente

### Pré-requisitos:
- Python 3.8+
- Docker
- Conta no GitHub

### Passos para configurar o ambiente:
1. Clone o repositório:

   ```bash
   git clone https://github.com/lucasfelipe01/pipeline_IOT
   cd pipeline_IOT
2. Crie e ative um ambiente virtual Python:

```bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows

3. Instale as dependências necessárias:

```bash
Copiar código
pip install pandas psycopg2-binary sqlalchemy streamlit plotly
Configure o banco de dados PostgreSQL com Docker:

4. Inicie o contêiner PostgreSQL:

```bash
Copiar código
docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
5. Carregue os dados CSV para o banco de dados:

Execute o script de processamento:

```bash
Copiar código
python pipeline.py
6. Execute o painel Streamlit:

```bash
Copiar código
streamlit run dashboard.py
Explicação das Views SQL
1. avg_temp_por_dispositivo
Descrição: Esta visualização calcula a temperatura média para cada dispositivo.
Insight: Permite identificar quais dispositivos estão reportando temperaturas consistentemente mais altas ou mais baixas.
sql
Copiar código
CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;
2. leituras_por_hora
Descrição: Esta visualização mostra uma contagem de leituras de temperatura agrupadas por hora.
Insight: Ajuda a identificar picos de atividade dos dispositivos ao longo do dia.
sql
Copiar código
CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora;
3. temp_max_min_por_dia
Descrição: Esta visualização calcula as temperaturas máximas e mínimas para cada dia.
Insight: Útil para monitorar variações extremas de temperatura ao longo do tempo.
sql
Copiar código
CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(timestamp) as data, MAX(temperature) as temp_max, MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY data;
