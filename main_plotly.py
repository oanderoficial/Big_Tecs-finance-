import pandas as pd
import plotly.express as px

#Grafico de linhas 
def plotar_dados_acoes(df, nome_acao):
    fig = px.line(df, x='Date', y='Volume', title=f'Desempenho da Ação {nome_acao}', template='plotly_dark')
    fig.show()

#Importando os dados em CSV 
opcao = ''
df_netflix = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/NFLX?period1=1022112000&period2=1705881600&interval=1d&events=history&includeAdjustedClose=true')
df_meta = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/META?period1=1337299200&period2=1705881600&interval=1d&events=history&includeAdjustedClose=true')
df_google = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1092873600&period2=1705881600&interval=1d&events=history&includeAdjustedClose=true')


#Menu de opções
while opcao != "0":
    print("1-Netflix, Inc. (NFLX)")
    print("2-Meta Platforms, Inc. (META)")
    print("3-Alphabet Inc. (GOOG)")
    print("0 - Sair do programa")
    opcao = input("Digite uma opção:")
    
    if opcao == '1':
        plotar_dados_acoes(df_netflix, 'Netflix, Inc. (NFLX)')
    elif opcao == '2':
        plotar_dados_acoes(df_meta, 'Meta Platforms, Inc. (META)')
    elif opcao == '3':
        plotar_dados_acoes(df_google, 'Alphabet Inc. (GOOG)')
    elif opcao == "0":
        print('Sair do Programa')
    else:
        print("Opção inválida")
