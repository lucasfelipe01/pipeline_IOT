# Pipeline de Dados IoT para Leituras de Temperatura

## Descrição do Projeto
Este projeto implementa um pipeline de dados para processar e armazenar leituras de temperatura de dispositivos IoT em um banco de dados PostgreSQL, utilizando Docker. A solução também inclui um dashboard interativo criado com Streamlit, que visualiza insights como a média de temperatura por dispositivo, leituras por hora e temperaturas máximas e mínimas por dia.

O fluxo de trabalho do projeto envolve:
- Processar um arquivo CSV (`IOT-temp.csv`) com leituras de temperatura de dispositivos IoT.
- Armazenar os dados em um banco de dados PostgreSQL usando SQLAlchemy.
- Criar visualizações dinâmicas dos dados via Streamlit.

---

## Como Configurar o Ambiente

### Pré-requisitos:
- Python 3.8+
- Docker
- Conta no GitHub e Kaggle

### Passos para configurar o ambiente:

1. Clone o repositório:
    ```bash
    git clone https://github.com/DOliveiira/pipeline-IOT
    cd repositorio
    ```

2. Crie e ative um ambiente virtual Python:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3. Instale as dependências necessárias:
    ```bash
    pip install pandas psycopg2-binary sqlalchemy streamlit plotly
    ```

4. Configure o banco de dados PostgreSQL com Docker:

    Inicie o contêiner PostgreSQL:
    ```bash
    docker run --name postgres-iot -e POSTGRES_PASSWORD=sua_senha -p 5432:5432 -d postgres
    ```

5. Carregue os dados CSV para o banco de dados:

    Execute o script de processamento:
    ```bash
    python pipeline.py
    ```

6. Execute o dashboard Streamlit:
    ```bash
    streamlit run dashboard.py
    ```

---

## Explicação das Views SQL

### 1. `avg_temp_por_dispositivo`
- **Descrição**: Esta view calcula a média de temperatura para cada dispositivo.
- **Insight**: Permite identificar quais dispositivos estão reportando temperaturas consistentemente mais altas ou mais baixas.
    ```sql
    CREATE VIEW avg_temp_por_dispositivo AS
    SELECT device_id, AVG(temperature) as avg_temp
    FROM temperature_readings
    GROUP BY device_id;
    ```

### 2. `leituras_por_hora`
- **Descrição**: Esta view mostra a contagem de leituras de temperatura agrupadas por hora.
- **Insight**: Ajuda a identificar picos de atividade dos dispositivos ao longo do dia.
    ```sql
    CREATE VIEW leituras_por_hora AS
    SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS contagem
    FROM temperature_readings
    GROUP BY hora;
    ```

### 3. `temp_max_min_por_dia`
- **Descrição**: Esta view calcula as temperaturas máxima e mínima para cada dia.
- **Insight**: Útil para monitorar variações extremas de temperatura ao longo do tempo.
    ```sql
    CREATE VIEW temp_max_min_por_dia AS
    SELECT DATE(timestamp) as data, MAX(temperature) as temp_max, MIN(temperature) as temp_min
    FROM temperature_readings
    GROUP BY data;
    ```

---

## Capturas de Tela do Dashboard

### 1. Média de Temperatura por Dispositivo
![image](https://github.com/user-attachments/assets/354bc1e3-e7be-415f-a25d-6eb4a5c1e13a)


### 2. Leituras por Hora do Dia
![image](https://github.com/user-attachments/assets/90cdb283-6f94-4884-baa7-9d3723bb5faf)


### 3. Temperaturas Máximas e Mínimas por Dia
![image](https://github.com/user-attachments/assets/34553a23-90a4-44b3-9dec-a32c91932baa)

