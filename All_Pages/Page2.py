import pandas as pd
import numpy as np
import os
import streamlit as st


def app():
    st.title("Analytics")

    df = pd.read_csv("C:/Users/rushi/Desktop/CS FILES/STREAMLIT/Sales Data/Sales_April_2019.csv")

    files = [file for file in os.listdir('C:/Users/rushi/Desktop/CS FILES/STREAMLIT/Sales Data')]

    Final_data = pd.DataFrame()

    for file in files:
        df = pd.read_csv("C:/Users/rushi/Desktop/CS FILES/STREAMLIT/Sales Data/" + file)
        Final_data = pd.concat([Final_data,df])
        
    Final_data.to_csv("Sales.csv",index=False)


    df1 = pd.read_csv("Sales.csv")



    df1['Quantity Ordered'] = pd.to_numeric(df1['Quantity Ordered'], errors='coerce')
    df1['Price Each'] = pd.to_numeric(df1['Price Each'], errors='coerce', downcast='float')



    df1.dropna(axis=0, inplace=True)
    df1['Quantity Ordered'].fillna(df1['Quantity Ordered'].median(), inplace=True)
    df1['Price Each'].fillna(df1['Price Each'].median(), inplace=True)
    df1['Order Date'] = pd.to_datetime(df1['Order Date'], errors='coerce')
    df1['Month'] = df1['Order Date'].dt.month.astype('Int32')
    df1['City'] = df1['Purchase Address'].str.split(',').str[1].str.strip()


    order_counts = df1.groupby('Product')['Quantity Ordered'].sum()


    product_counts_df = order_counts.reset_index()
    product_counts_df.columns = ['Product', 'Count']

    product_counts_df['Net Sales'] = df1.groupby('Product').apply(lambda x: (x['Quantity Ordered'] * x['Price Each']).sum()).reset_index(drop=True)



    df2 = df1.drop(['Order Date', 'Purchase Address','Order ID'], axis=1)
    df2 = df2.groupby(['Month','Product']).agg({
        'Quantity Ordered': 'sum',
        'Price Each': 'sum'
    }).reset_index()

    df3 = df1.drop(['Order Date', 'Purchase Address','Order ID'], axis=1)
    df3 = df3.groupby(['City','Product','Month']).agg({
        'Quantity Ordered': 'sum',
        'Price Each': 'sum'
    }).reset_index()

    # Month Wise Sales Graph Analysis

    import matplotlib.pyplot as plt

    df_month_1 = df2[df2['Month'] == 1]
    st.title("Month Wise Product Sales Bar Graph")
    st.bar_chart(df_month_1.set_index('Product')['Quantity Ordered'])

    # df1 = st.data_editor(df1)
    # product_counts_df = st.data_editor(product_counts_df)
    # df2 = st.data_editor(df2)
    # df3 = st.data_editor(df3)