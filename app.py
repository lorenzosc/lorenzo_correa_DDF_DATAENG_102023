import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import json

def main():
    st.title("Análise da quantidade de produtos conforme suas caracterizações")
    
    analysis_options = ["Material", "Número de features", "Categoria"]
    st.sidebar.header("Visualizações")
    analysis = st.sidebar.selectbox("Escolha a característa para contagem:", analysis_options)

    st.header(f"Distribuição da categoria \"{analysis}\"")

    #load dataframe
    data_path = r"/data/products_clean.json"
    with open(data_path) as json_file:
        products = json.load(json_file)
        df = pd.json_normalize(products["products"], max_level=0)
    df["features"] = df["features"][df["features"].notnull()].apply(lambda x: len(x))

    if analysis == "Material":
        count = df["material"].value_counts()

    if analysis == "Número de features":
        count = df["features"].value_counts()

    if analysis == "Categoria":
        count = df["product_category"].value_counts()

    sorted_count = count.sort_values(ascending=False)
    results = sorted_count.iloc[:8].copy()
    try:
        results["Other"] = sorted_count.iloc[8:].sum()
    except KeyError:
        pass

    fig = px.pie(results, values=results.values, names=results.index)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()  