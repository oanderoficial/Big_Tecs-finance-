import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

opcao = ''

def Netflix(): 
    df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/NFLX?period1=1514764800&period2=1681948800&interval=1d&events=history&includeAdjustedClose=true')
    df['Date'] = pd.to_datetime(df['Date'])
    dates = df['Date'].values
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Close', data=df)
    plt.title('Preço do fechamento das ações da Netflix ')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD)')
    plt.show()
  
def Meta():
    df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1514764800&period2=1681948800&interval=1d&events=history&includeAdjustedClose=true')
    df['Date'] = pd.to_datetime(df['Date'])
    dates = df['Date'].values
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Close', data=df)
    plt.title('Preço do fechamento das ações da Meta Platforms, Inc. (2018 até 2023)')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD)')
    plt.show()

def Google():
    df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1514764800&period2=1681948800&interval=1d&events=history&includeAdjustedClose=true')
    df['Date'] = pd.to_datetime(df['Date'])
    dates = df['Date'].values
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Close', data=df)
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
