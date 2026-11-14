# 🛒 Análise de Vendas de E-commerce (Olist)

Análise exploratória do **dataset público de e-commerce brasileiro da Olist** para responder perguntas de negócio com dados.

## ❓ Perguntas de negócio
1. Como as vendas evoluem mês a mês? Existe sazonalidade?
2. Qual é o **ticket médio** por pedido?
3. Quais **estados** mais compram?
4. Quais **categorias** geram mais receita?
5. Atraso na entrega afeta a **nota de avaliação**?

## 📂 Dados
[Brazilian E-Commerce Public Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce): cerca de 100 mil pedidos entre 2016 e 2018.

Baixe e descompacte os CSVs em `data/`:
```
data/
├── olist_orders_dataset.csv
├── olist_order_items_dataset.csv
├── olist_customers_dataset.csv
├── olist_products_dataset.csv
├── olist_order_reviews_dataset.csv
└── product_category_name_translation.csv
```

## 🧰 Tecnologias
Python, pandas, matplotlib, seaborn (rode como script ou copie as seções para um Jupyter Notebook)

## 🚀 Como rodar
```bash
git clone https://github.com/MoniqueSilva79/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis
pip install -r requirements.txt
# coloque os CSVs em data/
python analysis.py
```
Os gráficos são salvos em `outputs/`.

## 💡 Insights esperados (preencha com seus resultados)
- Pico de vendas em **novembro** (Black Friday)
- Concentração de pedidos no **Sudeste**, com SP na liderança
- Pedidos atrasados tendem a ter **notas bem menores**

## 📚 O que pratiquei
- Joins entre várias tabelas com pandas
- Análise exploratória (EDA) e métricas de negócio
- Visualização e comunicação de insights

## 🗺️ Próximos passos
- [ ] Análise RFM de clientes
- [ ] Dashboard no Looker Studio com BigQuery
