import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

opcao = ''
df_netflix = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/NFLX?period1=1022112000&period2=1705881600&interval=1d&events=history&includeAdjustedClose=true')
df_meta = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/META?period1=1337299200&period2=1705881600&interval=1d&events=history&includeAdjustedClose=true')
df_google = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1092873600&period2=1705881600&interval=1d&events=history&includeAdjustedClose=true')

def Netflix(): 
    dados = (df_netflix)
    df_netflix['Date'] = pd.to_datetime(df_netflix['Date'])
    dates = df_netflix['Date'].values
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Close', data=df_netflix)
    plt.title('Preço do fechamento das ações da Netflix (2004 até 2024) ')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD)')
    plt.show()
  
def Meta():
    dados = (df_meta)
    df_meta['Date'] = pd.to_datetime(df_meta['Date'])
    dates = df_meta['Date'].values
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Close', data=df_meta)
    plt.title('Preço do fechamento das ações da Meta Platforms, Inc. (2012 até 2024)')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD)')
    plt.show()

def Google():
    dados = (df_google)
    df_google['Date'] = pd.to_datetime(df_google['Date'])
    dates = df_google['Date'].values
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Close', data=df_google)
    plt.title('Preço do fechamento das ações da Google (2018 até 2023)')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD)')
    plt.show()

while opcao != "0":
    print("1-Netflix, Inc. (NFLX)")
    print("2-Meta Platforms, Inc. (META)")
    print("3-Alphabet Inc. (GOOG)")
    print("0 - Sair do programa")
    opcao = input("Digite uma opção:")
    if opcao == '1':
        Netflix()
    elif opcao == '2':
        Meta()
    elif opcao == '3':
        Google()
    elif opcao == "0":
        print('Sair do Programa')
    else:
        print("Opção inválida")
