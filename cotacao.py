import asyncio
import os
import requests
import json

# Obtém a chave da API a partir da variável de ambiente
api_Key = os.getenv("EXCHANGE_API_KEY")

if not api_Key:
    print("Erro: Variável de ambiente 'EXCHANGE_API_KEY' não encontrada.")
    exit(1)

#faz a requisicao para obter os precos da cotacao do dia
async def obter_taxas():
    url_Requisicao = f"https://v6.exchangerate-api.com/v6/{api_Key}/latest/USD"
    try:
        requisicao = requests.get(url_Requisicao)
        requisicao.raise_for_status()
        return requisicao.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

#faz a busca de moedas correspondentes ao termo buscado dentro de um arquivo json e devolve o resultado da busca
def busca_nome_moeda(palavra):
    try:
        with open('moedas.json', 'r', encoding='utf-8') as file:
            dados = json.load(file)

        resultado_nome = []
        resultado_sigla = []

        for sigla, moeda in dados.items():
            if palavra.lower() in moeda.lower():
                resultado_nome.append(moeda)
                resultado_sigla.append(sigla)

        if not resultado_nome:
            print("Nenhuma moeda encontrada para o nome fornecido.")
        return resultado_nome, resultado_sigla
    except FileNotFoundError:
        print("Arquivo moedas.json não encontrado!")
        return [], []

#mostra o valor de uma moeda em relacao ao dolar americano
def busca_moeda(taxas):
    moeda_nome = input("Digite o nome da moeda que deseja encontrar:\n")                
    dados = taxas
    if dados is None:
        print("Erro ao buscar dados da api")
    else:
        taxas = dados["conversion_rates"]            
        nomes, siglas = busca_nome_moeda(moeda_nome)
        if not nomes:
            print("Termo informado nao consta na base de dados ou eh invalido")
        
    
        print(f"\nCotações de {moeda_nome.title()}:")
        mostrar_taxas(nomes, siglas, taxas)
        print("\n---------------------------------------------------\n")        

#converte um determinado valor entre o dolar americano(padrao) e outra moeda escolhida
def converte_moeda(taxas):
    valor_bruto=int(input("Digite o valor inicial para ser convertido:\n"))
    moeda_nome = input("Digite o nome da moeda que deseja encontrar:\n")                
    dados = taxas
    if dados is None:
        print("Erro ao buscar dados da api")  
    else:      
        taxas = dados["conversion_rates"]            
        nomes, siglas = busca_nome_moeda(moeda_nome)
        if not nomes:
            print("Termo informado nao consta na base de dados ou eh invalido")
        
        print(f"\nCotações de {moeda_nome.title()}:")
        mostra_valor_convertido(nomes, siglas, taxas,valor_bruto)
        print("\n---------------------------------------------------\n")
    
#mostra a taxa dos resultados obtidos na busca em relação ao dolar americano(padrao)
def mostrar_taxas(nomes, siglas, taxas):
    for moeda, taxa in taxas.items():
        for i in range(len(siglas)):
            if siglas[i] == moeda:
                print(f"{nomes[i]} ({siglas[i]}): {taxa}")

#mostra o valor de uma quantidade de dolares americanos(padrao) em uma moeda que o usuario escolha
def mostra_valor_convertido(nomes, siglas, taxas,valor_bruto):
    for moeda, taxa in taxas.items():
        for i in range(len(siglas)):
            if siglas[i] == moeda:
                print(f"{nomes[i]} ({siglas[i]}): {taxa*valor_bruto}")

async def main():
    while True:
        taxas= await obter_taxas()
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---------------------------------------------------")
        print("Consulta cotacao do dia:")
        print("---------------------------------------------------")
        print("1 - Consultar valor de moeda em relação ao dolar")
        print("2 - Converter valor entre moedas especificas")
        print("3 - Sair")
        opc=int(input("Digite uma opcao:\n"))
        
        if (opc==1):
            busca_moeda(taxas)
            print("Pressione Enter para continuar...")
            input()
        if (opc==2):                        
            converte_moeda(taxas)
            print("Pressione Enter para continuar...")
            input()
        if (opc==3):
            print("Saindo do programa...")
            break
  
asyncio.run(main())
