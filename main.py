import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

opcao = ''

while opcao != "0":
  print("1-Netflix, Inc. (NFLX)")
  print("2-Meta Platforms, Inc. (META)")
  print("3-Alphabet Inc. (GOOG)")
  print("0 - Sair do programa")
  opcao = input("Digite uma opção:")

  if opcao == '1':

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

  elif opcao == '2':

    df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/META?period1=1514764800&period2=1681948800&interval=1d&events=history&includeAdjustedClose=true')
    df['Date'] = pd.to_datetime(df['Date'])
    dates = df['Date'].values
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Close', data=df)
    plt.title('Preço do fechamento das ações da Meta (2018 até 2023')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD)')
    plt.show()

  elif opcao == '3':

    df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1514764800&period2=1681948800&interval=1d&events=history&includeAdjustedClose=true')
    df['Date'] = pd.to_datetime(df['Date'])
    dates = df['Date'].values
    sns.set_style('darkgrid')
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Date', y='Close', data=df)
    plt.title('Preço do fechamento das ações da Google (2018 até 2023')
    plt.xlabel('Data')
    plt.ylabel('Preço de fechamento (USD)')
    plt.show()

print('Sair do Programa')
