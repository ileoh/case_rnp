# limpeza.py

# 1. Configurações Iniciais
import pandas as pd
from google.cloud import storage

# Constantes
GCP_STORAGE_BUCKET = 'your_gcp_storage_bucket'
GCP_BIGQUERY_TABLE = 'your_gcp_bigquery_table'

# 2. Funções de Limpeza
def remove_duplicates(df):
    return df.drop_duplicates()

def handle_missing_values(df, strategy='mean'):
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'drop':
        return df.dropna()

# 3. Funções de Transformação
def convert_to_numeric(df, column):
    df[column] = pd.to_numeric(df[column], errors='coerce')
    return df

# 4. Funções de Verificação de Qualidade
def check_missing_values(df):
    return df.isnull().sum()

def check_duplicate_values(df):
    return df.duplicated().sum()

# 5. Envio para o GCP
def upload_to_gcp_storage(df, file_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(GCP_STORAGE_BUCKET)
    blob = bucket.blob(file_name)
    blob.upload_from_string(df.to_csv(index=False), 'text/csv')

# Função Principal
def main():
    # Suponha que o DataFrame df contenha os dados coletados
    # df = pd.read_csv('path/to/your/raw/data.csv')
    
    # Limpeza de Dados
    df = remove_duplicates(df)
    df = handle_missing_values(df)
    
    # Transformação de Dados
    df = convert_to_numeric(df, 'some_numeric_column')
    
    # Verificação de Qualidade
    print('Missing values:', check_missing_values(df))
    print('Duplicate values:', check_duplicate_values(df))
    
    # Envio para o GCP
    upload_to_gcp_storage(df, 'cleaned_data.csv')

# Inicializando a limpeza de dados
if __name__ == "__main__":
    main()
