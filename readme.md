# PROCESSO SELETIVO DA DADOSFERA PARA ENGENHARIA DE DADOS

## ITEM 1

[Vídeo](link)

## ITEM 2

O dataset foi baixado e transformado no formato adequado utilizando os códigos [jsonl_to_csv.py](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/main/jsonl_to_csv.py) e posteriormente o [divide_csv.py](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/main/divide_csv.py) devido ao tamanho acima do limitado para upload no site. Como eram muitos dados, as análises foram feitas apenas em cima de produtos que estavam na primeira divisão, e, dessa forma, apenas a primeira divisão foi catalogada na Dadosfera. Os dados podem ser encontrados em:

[Dataset](https://app.dadosfera.ai/pt-BR/catalog/data-assets/812f5bb6-be86-4c27-b867-5bb20b807568)

![Foto do Dataset](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/main/raw_dataset.png)

## ITEM 3

A extração de features dos produtos foram feitas através da utilização da API do chatGPT, biblioteca openai do python.
O código [openai_usage.py](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/main/openai_usage.py) realiza extrações de forma assincrona, mas se limita em fazer no máximo 3 requisições por vez para não exceder o máximo de tokens por minuto que a API aceita. A mensagem utilizada como prompt para o chatGPT ser vista [aqui](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/c59e024425f2d1eb48b80b814905ad9dbbf4da04/openai_usage.py#L23-L25).

As features foram registradas em um arquivo json, e depois transformadas em CSV para upload novamente na Dadosfera
com uso do código [products_json_to_csv.py](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/main/products_json_to_csv.py).

[Dataset](https://app.dadosfera.ai/pt-BR/catalog/data-assets/4b486b91-1e30-43f5-b8e2-9e5fe22e51d1)

![Foto do Dataset](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/main/features_dataset.png)

## ITEM 4

Utilizando do módulo de visualização, foram feitas perguntas em SQL para o banco de dados e os gráficos gerados foram
colocados em um dashboard. Como as categorias de produtos foram geradas automaticamente, aquelas categorias onde só
foi encontrado 1 produto foram ignoradas na segunda query, dando outra possibilidade de insight sobre os produtos.

[SQL Query](https://metabase-treinamentos.dadosfera.ai/question/469-product-categories)

[SQL Query 2](https://metabase-treinamentos.dadosfera.ai/question/468-product-categories-without-uniques)

[Dashboard](https://metabase-treinamentos.dadosfera.ai/dashboard/58-categorias-de-produtos)

![Todos as categorias](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/main/Product%20categories-02_11_2023%2C%2018_35_20.png)
![Sem as categorias de apenas 1 produto](https://github.com/lorenzosc/lorenzo_correa_DDF_DATAENG_102023/blob/main/Product%20categories%20without%20uniques-02_11_2023%2C%2018_35_23.png)

## ITEM 5

[Dataapp](https://app-intelligence-treinamentos.dadosfera.ai/pbp-service-visualizacao-bc5e29e5-4fee-4f6430458f0b-905e-4aaf_8501/)

O Data app foi criado para facilitar a verificação da quantidade de produtos por categoria, material ou número de features conforme foi caracterizado no ITEM 3 pelo chatGPT.