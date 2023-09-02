# 📚 Projeto de Hub de Dados para Educação Brasileira (RNP)

## 🎯 Objetivo

Este projeto visa criar um hub de dados centralizado para coletar, transformar e analisar dados educacionais de várias organizações parceiras no Brasil. O objetivo principal é entender a dinâmica da evasão escolar e identificar maneiras de preveni-la.

## 🛠️ Componentes Principais

- **Ingestão de Dados**: Google Cloud Functions
- **Armazenamento de Dados**: Google Cloud Storage e BigQuery
- **Análise de Dados**: BigQuery e Google Data Studio

## 🗂️ Estrutura do Repositório

```text
📦 Projeto_Hub_Educacao/
├── 📄 codigo/
│   ├── 🐍 ingestao.py
│   └── 🧹 limpeza.py
├── 📊 dados_exemplo/
│   ├── 📋 brutos/
│   │   ├── 🗃️ dados_banco_relacional.csv
│   │   ├── 📄 dados_csv.csv
│   │   └── 🌐 dados_api.json
│   └── 📋 limpos/
│       ├── 🗃️ dados_banco_relacional_limpos.csv
│       ├── 📄 dados_csv_limpos.csv
│       └── 🌐 dados_api_limpos.json
├── 📐 diagramas/
│   ├── 🏗️ arquitetura.png
│   └── 🚀 fluxo_dados.png
├── 📚 documentacao/
│   ├── 🌐 Arquitetura_Sistema.md
│   ├── 📈 Fluxo_Dados.md
│   ├── 🔄 Modelo_Interoperabilidade.md
│   ├── 🔒 Compliance_LGPD.md
│   └── 📖 Manual_Usuario.md
└── 📋 requirements.txt
```

## 📝 Descrição das Pastas e Arquivos

- **📄 codigo/**: Contém os scripts de ingestão e limpeza dos dados.
- **📊 dados_exemplo/**: Contém exemplos de dados brutos e limpos.
- **📐 diagramas/**: Contém diagramas ilustrando a arquitetura e o fluxo de dados.
- **📚 documentacao/**: Contém toda a documentação do projeto, incluindo arquitetura do sistema, conformidade com a LGPD e manual do usuário.
- **📋 requirements.txt**: Lista de todas as dependências necessárias para rodar os scripts.

## 🚀 Iniciando

### 📋 Pré-requisitos

- Python 3.x
- Google Cloud SDK
- Conta no Google Cloud Platform (GCP)

### 🛠️ Instalação

1. Clone este repositório.
2. Vá para o diretório do projeto e instale as dependências utilizando:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure suas credenciais GCP seguindo o [Manual do Usuário](documentacao/Manual_Usuario.md).

### 📖 Uso

Para mais detalhes sobre como usar este projeto, consulte o [Manual do Usuário](documentacao/Manual_Usuario.md).

## 📜 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE.md](LICENSE.md) para detalhes.