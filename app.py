import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1-Importando os Dados
data = pd.read_csv("data/Pedidos.csv")
df = pd.DataFrame(data)

def main():
    st.title("Dashboard de Vendas :shopping_trolley:")
    
    aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
    with aba1:
        display_dataframe(df)
    with aba2:
        display_charts(df)
    with aba3:
        display_metrics(df)
    
#Função para exibir o DataFrame
def display_dataframe(data):
    st.header("Visualização do DataFrame")
    st.sidebar.header("Filtros")
    selected_region = st.sidebar.multiselect(
        "Selecione as regiões",
        data['Regiao'].unique(),
        data['Regiao'].unique()
    )
    filtered_data = data[data['Regiao'].isin(selected_region)]
    st.write(filtered_data)

#Função para exibir os gráficos
def display_charts(data):
    st.header("Visualização de Gráficos")
    st.set_option("deprecation.showPyplotGlobalUse", False)
    
    #Gráfico 1: Desempenho por Região
    st.subheader("Desempenho por Região")
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Regiao", data=data)
    st.pyplot()
    
    #Gráfico 2: Itens mais vendidos
    st.subheader("Itens mais Vendidos")
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Item", data=data)
    st.pyplot()
    
    #Gráfico 3: Preço Médio por Item
    st.subheader("Preço Médio por Item")
    avg_price = data.groupby("Item")["PrecoUnidade"].mean().sort_values(ascending=False)
    st.write(avg_price)
    
#Função para exibir métricas
def display_metrics(data):
    st.subheader("Métricas")
    
    #Métricas simples
    total_sales = data["Unidades"].sum()
    average_price = data["PrecoUnidade"].mean()
    most_productive = data["Vendedor"].value_counts().idxmax()
    
    coluna1, coluna2, coluna3 = st.columns(3)
    with coluna1:
        st.metric("O vendedor mais produtivo foi:",most_productive)
    with coluna2:
        st.metric("Vendas Totais:", total_sales)
    with coluna3:
        st.metric("Preço Médio:", round(average_price, 2))
    
#Execução do aplicativo
if __name__ == "__main__":
    main()