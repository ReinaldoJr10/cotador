class MoedaView:
    @staticmethod
    def exibir_opcoes():
        print("---------------------------------------------------")
        print("Consulta cotacao do dia:")
        print("---------------------------------------------------")
        print("1 - Consultar valor de moeda em relação ao dolar")
        print("2 - Converter valor entre moedas especificas")
        print("3 - Receber recomendacoes com base no gps")
        print("4 - Sair")
        opc = int(input("Digite uma opcao:\n"))
        return opc

    @staticmethod
    def exibir_resultado_busca(nomes, siglas, taxas):
        print(f"\nCotações de {nomes[0].title()}:")
        for moeda, taxa in taxas.items():
            for i in range(len(siglas)):
                if siglas[i] == moeda:
                    print(f"{nomes[i]} ({siglas[i]}): {taxa}")

    @staticmethod
    def exibir_valor_convertido(nomes, siglas, taxas, valor_bruto):
        for moeda, taxa in taxas.items():
            for i in range(len(siglas)):
                if siglas[i] == moeda:
                    print(f"{nomes[i]} ({siglas[i]}): {taxa * valor_bruto}")
