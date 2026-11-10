# Earthquake Data Pipeline

## 1. Sobre o projeto

Este projeto consiste no desenvolvimento de um pipeline ETL (Extract, Transform, Load) para coletar, tratar e armazenar dados de terremotos disponibilizados pelo USGS (United States Geological Survey).

O objetivo é construir um processo automatizado de integração de dados utilizando Python e PostgreSQL, aplicando conceitos fundamentais de Engenharia de Dados.

## 2. Arquitetura do projeto

O pipeline é dividido em três etapas principais:

**Extract**
- Consumo da API pública do USGS.
- Recebimento dos dados no formato GeoJSON.
- Armazenamento dos dados brutos em formato JSON.

**Transform**
- Normalização dos dados utilizando Pandas.
- Seleção dos campos relevantes.
- Conversão dos timestamps para datetime.
- Separação das coordenadas geográficas em longitude, latitude e profundidade.
- Padronização dos nomes das colunas.

**Load**
- Conexão com PostgreSQL utilizando SQLAlchemy.
- Criação da tabela earthquakes.
- Inserção e atualização dos registros.
- Utilização de UPSERT para evitar duplicações com base no identificador único do evento.

## 3. Tecnologias utilizadas

- Python
- Pandas
- Requests
- PostgreSQL
- SQLAlchemy
- Psycopg
- Docker
- Git e GitHub

## 4. Fonte dos dados

Os dados são obtidos através do USGS Earthquake Hazards Program.

API utilizada: USGS GeoJSON Feed

https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson

## 5. Estrutura do projeto

```text
earthquake-data-pipeline/
│
├── data/
│   └── raw/
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── database/
│   │   ├── connection.py
│   │   └── create_table.py
│   │
│   ├── extract/
│   │   └── extract.py
│   │
│   ├── load/
│   │   └── load.py
│   │
│   └── transformation/
│       └── transformation.py
│
├── .env.example
├── .gitignore
└── requirements.txt
```

## 6. Campos armazenados

| Campo | Descrição |
|---|---|
| event_id | Identificador único do terremoto |
| magnitude | Magnitude do evento |
| place | Localização descrita pelo USGS |
| event_time | Data e hora do evento |
| updated_at | Data e hora da última atualização |
| event_url | Link para os detalhes do evento |
| longitude | Coordenada geográfica |
| latitude | Coordenada geográfica |
| depth | Profundidade do terremoto |

## 7. Como executar o projeto

### Pré-requisitos

- Python instalado
- Docker instalado
- PostgreSQL em execução
- Ambiente virtual Python configurado

### Instalação das dependências

```bash
pip install -r requirements.txt
```

### Configuração das variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto, utilizando o `.env.example` como modelo.

Configure os dados de conexão com o PostgreSQL.

### Criação da tabela

```bash
python -m src.database.create_table
```

### Execução do pipeline

```bash
python -m src.load.load
```

O pipeline executará a extração dos dados, a transformação e a carga no PostgreSQL.

## 8. Estratégia de carga

A carga utiliza UPSERT com `event_id` como chave primária.

Quando um evento já existe, seus dados são atualizados. Quando um novo evento é recebido, ele é inserido na tabela.

Essa estratégia permite executar o pipeline novamente sem criar registros duplicados.

## 9. Objetivos de aprendizagem

Este projeto foi desenvolvido para aplicar conceitos fundamentais de Engenharia de Dados:

- Consumo de APIs.
- Manipulação de dados JSON.
- Extração e transformação de dados.
- Modelagem de tabelas relacionais.
- Integração Python e PostgreSQL.
- Cargas com UPSERT.
- Organização de projetos Python.
- Controle de versão com Git e GitHub.