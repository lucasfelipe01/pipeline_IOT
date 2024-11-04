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
- Conta no GitHub e no Kaggle

### Passos para configurar o ambiente:
1. Clone o repositório:

   ```bash
   git clone https://github.com/lucasfelipe01/pipeline_IOT
   cd pipeline_IOT
2. Crie e ative um ambiente virtual Python:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate      # Windows

3. Instale as dependências necessárias:

   ```bash
   pip install pandas psycopg2-binary sqlalchemy streamlit plotly

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

6. Execute o painel Streamlit:

```bash
streamlit run dashboard.py
```

## Explicação das Views SQL
1.avg_temp_por_dispositivo
Descrição : Esta visualização calcula a temperatura média para cada dispositivo.
Insight : Permite identificar quais dispositivos estão reportando temperaturas consistentemente mais altas ou mais baixas.
```sql
CREATE VIEW avg_temp_por_dispositivo AS
SELECT device_id, AVG(temperature) as avg_temp
FROM temperature_readings
GROUP BY device_id;
```

2.leituras_por_hora
Descrição : Esta visualização mostra uma contagem de leituras de temperatura agrupadas por hora.
Insight : Ajuda a identificar picos de atividade dos dispositivos ao longo do dia.
```sql
CREATE VIEW leituras_por_hora AS
SELECT EXTRACT(HOUR FROM timestamp) AS hora, COUNT(*) AS contagem
FROM temperature_readings
GROUP BY hora;
```

3.temp_max_min_por_dia
Descrição : Esta visualização calcula as temperaturas máximas e mínimas para cada dia.
Insight : Útil para monitorar variações extremas de temperatura ao longo do tempo.
```sql
CREATE VIEW temp_max_min_por_dia AS
SELECT DATE(timestamp) as data, MAX(temperature) as temp_max, MIN(temperature) as temp_min
FROM temperature_readings
GROUP BY data;
```


##Capturas de Tela do Dashboard




1. Média de temperatura por dispositivo: 
![Captura de tela 2024-11-03 123323](https://github.com/user-attachments/assets/fdab9ddf-4967-4224-80a3-8330230c8d86)
2. Leituras por Hora do Dia:
![Captura de tela 2024-11-03 123435](https://github.com/user-attachments/assets/cd8054f2-07cd-43f1-865b-d02321e20d51)
3. Temperaturas Máximas e Mínimas por Dia: 
![Captura de tela 2024-11-03 123454](https://github.com/user-attachments/assets/190c1c17-9d03-420a-bff2-e66b861db6c0)


