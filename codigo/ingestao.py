# ingestao.py

# Configurações Iniciais
import os
import requests
import csv
import pymysql
from google.cloud import storage
import logging

# Constantes (essas informações devem ser armazenadas de forma segura, não diretamente no código)
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_NAME = os.environ.get('DB_NAME')

GCP_STORAGE_BUCKET = os.environ.get('GCP_STORAGE_BUCKET')

# Configurar logging
logging.basicConfig(level=logging.INFO)

# Funções de Auxílio
def get_db_connection():
    try:
        return pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
    except Exception as e:
        logging.error(f"Erro ao conectar com o banco de dados: {e}")

def get_api_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Erro ao buscar dados da API: {e}")

def upload_to_gcp_storage(file_name, file_path):
    try:
        storage_client = storage.Client()
        bucket = storage_client.get_bucket(GCP_STORAGE_BUCKET)
        blob = bucket.blob(file_name)
        blob.upload_from_filename(file_path)
    except Exception as e:
        logging.error(f"Erro ao fazer upload para o GCP Storage: {e}")

# Ingestão de Dados do Banco Relacional
def fetch_relational_data():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM your_table;"
        cursor.execute(query)
        data = cursor.fetchall()

        # TODO: Trate e armazene os dados em conformidade com a LGPD antes de enviá-los.

        # TODO: Envie os dados para o GCP (Cloud Storage, BigQuery)
        upload_to_gcp_storage('relational_data.csv', '/path/to/your/csv')

# Ingestão de Dados de Arquivos CSV
def fetch_csv_data(file_path):
    try:
        data = []
        with open(file_path, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                data.append(row)
        
        # TODO: Trate e armazene os dados em conformidade com a LGPD antes de enviá-los.

        # TODO: Envie os dados para o GCP (Cloud Storage, BigQuery)
        upload_to_gcp_storage('csv_data.csv', '/path/to/your/csv')
    except Exception as e:
        logging.error(f"Erro ao ler o arquivo CSV: {e}")

# Ingestão de Dados de API
def fetch_api_data(api_url):
    data = get_api_data(api_url)
    if data:
        # TODO: Trate e armazene os dados em conformidade com a LGPD antes de enviá-los.

        # TODO: Envie os dados para o GCP (Cloud Storage, BigQuery)
        upload_to_gcp_storage('api_data.json', '/path/to/your/json')

# Inicializando ingestão de dados
if __name__ == "__main__":
    fetch_relational_data()
    fetch_csv_data('/path/to/your/csv')
    fetch_api_data('https://api.your_source.com/data')
