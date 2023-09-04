# Manual do Usuário

## Introdução

Este manual foi criado para ajudá-lo a entender como configurar e utilizar o sistema de gestão de dados empresariais. Ele abrange os principais aspectos, desde a instalação das dependências até o uso avançado dos scripts de ingestão e limpeza de dados.

---

## Índice

1. [Pré-Requisitos](#pré-requisitos)
2. [Instalação](#instalação)
3. [Configuração](#configuração)
4. [Uso Básico](#uso-básico)
5. [Uso Avançado](#uso-avançado)
6. [Cenários de Utilização](#cenários-de-utilização)
7. [Solução de Problemas](#solução-de-problemas)

---

## Pré-Requisitos

- Python 3.8 ou superior
- Conta no Google Cloud Platform (GCP)
- Acesso ao serviço Google Cloud Storage e BigQuery

---

## Instalação

### Instalando Python

Certifique-se de que possui Python 3.8 ou superior instalado. Você pode verificar isso abrindo um terminal e digitando:

```bash
python --version
```

### Dependências

Clone o repositório e instale as dependências utilizando o seguinte comando:

```bash
pip install -r requirements.txt
```

---

## Configuração

### Variáveis de Ambiente

Configure as variáveis de ambiente referentes ao seu banco de dados e ao GCP. Edite o arquivo `.env` na pasta raiz e preencha as informações correspondentes.

### Permissões GCP

Certifique-se de ter configurado as permissões corretas no GCP para acessar os serviços de armazenamento e BigQuery.

---

## Uso Básico

### Ingestão de Dados

Execute o script `ingestao.py` para iniciar o processo de ingestão de dados. Abra um terminal na pasta onde o script está localizado e digite:

```bash
python ingestao.py
```

### Limpeza de Dados

Para iniciar a limpeza dos dados, execute o script `limpeza.py`:

```bash
python limpeza.py
```

---

## Uso Avançado

### Alterando Configurações de Ingestão

As configurações de ingestão podem ser modificadas diretamente no script `ingestao.py`. Leia a documentação interna do código para entender como fazer essas mudanças.

### Customizando a Limpeza de Dados

Da mesma forma, o script `limpeza.py` possui diversas opções para personalização. Consulte a documentação interna para mais informações.

---

## Cenários de Utilização

O sistema foi desenvolvido para suportar dois cenários principais:

1. **Alta Performance**: Para cenários que requerem alta velocidade e eficiência.
2. **Custo-Efetivo**: Para cenários onde o custo é uma consideração importante.

Para mais informações sobre como alternar entre esses cenários, consulte o documento `README.md`.

---


