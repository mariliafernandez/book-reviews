# Book Reviews

Este repositório contém os códigos para as análises dos dados em `books_data.csv` e `Books_rating.csv`

## Dependências
As dependências deste projeto estão em `Pipfile`.
A pasta deve estar estruturada na seguinte maneira e com os arquivos `books_data.csv` e `Books_rating.csv`:

root
│   Pipfile
│   readme.md
│   sentiment.py
│   clustering.py
└───data
        books_data.csv
        Books_rating.csv

## Análise de Sentimento
Executar o script `sentiment.py` para gerar `data/sentiment.csv`

```bash
python sentiment.py
```

## Clustering de Gêneros Literários
Executar o script `clustering.py` para gerar `data/clusters.csv`

```bash
python clustering.py
```