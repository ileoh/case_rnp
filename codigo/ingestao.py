# ingestao.py

# 1. Configurações Iniciais
import requests
import csv
import pymysql
from google.cloud import storage

# Constantes
DB_HOST = 'your_db_host'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'
DB_NAME = 'your_db_name'

GCP_STORAGE_BUCKET = 'your_gcp_storage_bucket'
GCP_BIGQUERY_TABLE = 'your_gcp_bigquery_table'

SCENARIO = "high_performance"  # Altere para "cost_effective" para cenário de custo efetivo

# 2. Funções de Auxílio
def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

def get_api_data(url):
    response = requests.get(url)
    return response.json()

def upload_to_gcp_storage(file_name, file_path):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(GCP_STORAGE_BUCKET)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_path)

# 3. Ingestão de Dados do Banco Relacional
def fetch_relational_data():
    connection = get_db_connection()
    cursor = connection.cursor()
    
    if SCENARIO == "high_performance":
        query = "SELECT * FROM your_table;"
    else:
        query = "SELECT * FROM your_table LIMIT 1000;"
        
    cursor.execute(query)
    data = cursor.fetchall()
    
    upload_to_gcp_storage('relational_data.csv', '/path/to/your/csv')

# 4. Ingestão de Dados de Arquivos CSV
def fetch_csv_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    
    upload_to_gcp_storage('csv_data.csv', '/path/to/your/csv')

# 5. Ingestão de Dados de API
def fetch_api_data(api_url):
    data = get_api_data(api_url)
    
    if SCENARIO == "cost_effective":
        # Suponhamos que temos uma forma de limitar a quantidade de dados baixados em um cenário de custo efetivo
        data = data[:100]
    
    upload_to_gcp_storage('api_data.json', '/path/to/your/json')

# 6. Inicializando ingestão de dados
if __name__ == "__main__":
    fetch_relational_data()
    fetch_csv_data('/path/to/your/csv')
    fetch_api_data('https://api.your_source.com/data')
