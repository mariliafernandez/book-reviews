# Book Reviews

Este repositório contém os códigos para as análises dos dados em `books_data.csv` e `Books_rating.csv`

## Requisitos e Dependências
As dependências deste projeto estão em `requirements.txt`.

A pasta deve estar estruturada na seguinte maneira e com os arquivos `books_data.csv` e `Books_rating.csv` dentro de `data/`:

```
root/
├── readme.md
├── requirements.txt
├── src/
│   ├── clustering.py
│   └── sentiment.py
└── data/
    └── books_data.csv
    └── Books_rating.csv
```

## Análise de Sentimento
Executar o script `sentiment.py` para gerar o arquivo `data/sentiment.csv`

```bash
python src/sentiment.py
```

## Clustering de Gêneros Literários
Executar o script `clustering.py` para gerar o arquivo `data/clusters.csv`

```bash
python src/clustering.py
```