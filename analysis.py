"""Análise exploratória de vendas – dataset público Olist."""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

DATA = Path("data")
OUT = Path("outputs")
OUT.mkdir(exist_ok=True)
sns.set_theme(style="whitegrid")

# ---------- Carga ----------
orders = pd.read_csv(DATA / "olist_orders_dataset.csv",
                     parse_dates=["order_purchase_timestamp", "order_delivered_customer_date",
                                  "order_estimated_delivery_date"])
items = pd.read_csv(DATA / "olist_order_items_dataset.csv")
customers = pd.read_csv(DATA / "olist_customers_dataset.csv")
products = pd.read_csv(DATA / "olist_products_dataset.csv")
reviews = pd.read_csv(DATA / "olist_order_reviews_dataset.csv")
translation = pd.read_csv(DATA / "product_category_name_translation.csv")

delivered = orders[orders["order_status"] == "delivered"]
df = (delivered.merge(items, on="order_id")
               .merge(customers, on="customer_id")
               .merge(products, on="product_id", how="left"))
df["receita"] = df["price"] + df["freight_value"]

# ---------- 1. Vendas mensais ----------
mensal = df.set_index("order_purchase_timestamp").resample("MS")["receita"].sum()
mensal.plot(figsize=(10, 4), marker="o", title="Receita mensal (R$)")
plt.tight_layout(); plt.savefig(OUT / "1_receita_mensal.png"); plt.close()

# ---------- 2. Ticket médio ----------
ticket = df.groupby("order_id")["receita"].sum().mean()
print(f"Ticket médio por pedido: R$ {ticket:,.2f}")

# ---------- 3. Estados ----------
estados = df.groupby("customer_state")["order_id"].nunique().sort_values(ascending=False).head(10)
estados.plot(kind="bar", figsize=(8, 4), title="Top 10 estados por nº de pedidos")
plt.tight_layout(); plt.savefig(OUT / "2_top_estados.png"); plt.close()

# ---------- 4. Categorias ----------
cat = (df.merge(translation, on="product_category_name", how="left")
         .groupby("product_category_name_english")["receita"].sum()
         .sort_values(ascending=False).head(10))
cat.sort_values().plot(kind="barh", figsize=(8, 5), title="Top 10 categorias por receita (R$)")
plt.tight_layout(); plt.savefig(OUT / "3_top_categorias.png"); plt.close()

# ---------- 5. Atraso x avaliação ----------
d = delivered.merge(reviews[["order_id", "review_score"]], on="order_id")
d["atrasado"] = d["order_delivered_customer_date"] > d["order_estimated_delivery_date"]
notas = d.groupby("atrasado")["review_score"].mean()
print("\nNota média de avaliação:")
print(notas.rename({False: "No prazo", True: "Atrasado"}).round(2))
sns.barplot(x=notas.index.map({False: "No prazo", True: "Atrasado"}), y=notas.values)
plt.title("Nota média: entregas no prazo x atrasadas"); plt.ylabel("Nota (1-5)")
plt.tight_layout(); plt.savefig(OUT / "4_atraso_vs_nota.png"); plt.close()

print(f"\nGráficos salvos em {OUT.resolve()}")
