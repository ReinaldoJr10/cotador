import json

class MoedaModel:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla

    @staticmethod
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
            return resultado_nome, resultado_sigla
        except FileNotFoundError:
            print("Arquivo moedas.json não encontrado!")
            return [], []
    @staticmethod
    def busca_nome_moeda_sigla(sigla_busca):
        try:
            with open('moedas.json', 'r', encoding='utf-8') as file:
                dados = json.load(file)
            resultado_nome = []
            resultado_sigla = []
            for sigla, moeda in dados.items():
                if sigla_busca.lower() in sigla.lower():
                    resultado_nome.append(moeda)
                    resultado_sigla.append(sigla)
            return resultado_nome, resultado_sigla
        except FileNotFoundError:
            print("Arquivo moedas.json não encontrado!")
            return [], []