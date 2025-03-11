import json
from models.taxa_model import TaxaModel
from views.moeda_view import MoedaView
from models.moeda_model import MoedaModel
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

class MoedaController:
    def __init__(self, api_key):
        self.api_key = api_key
        self.taxas=[]
        self.atualizar_taxas()

    def consultar_taxa(self):
        moeda_nome = input("Digite o nome da moeda que deseja encontrar:\n")
        nomes, siglas = MoedaModel.busca_nome_moeda(moeda_nome)
        if not nomes:
            print("Termo informado não consta na base de dados ou é inválido.")
            return
        MoedaView.exibir_resultado_busca(nomes, siglas, self.taxas)

    def converter_moeda(self):
        valor_bruto = int(input("Digite o valor inicial para ser convertido:\n"))
        moeda_nome = input("Digite o nome da moeda que deseja encontrar:\n")
        nomes, siglas = MoedaModel.busca_nome_moeda(moeda_nome)
        if not nomes:
            print("Termo informado não consta na base de dados ou é inválido.")
            return
        MoedaView.exibir_valor_convertido(nomes, siglas, self.taxas, valor_bruto)
        
    def moeda_cidade(self,cidade_ref,n=10):
        lista_cidades=[]
        try:
            with open('dados.json','r',encoding='utf-8') as arq:
                dados= json.load(arq)
            for dado in dados:            
                n1 = float(dados[dado]["latitude"])
                n2 = float(dados[dado]["longitude"])
                distancia_cidade = geodesic(cidade_ref,(n1,n2)).kilometers
                lista_cidades.append((dado,distancia_cidade))
            lista_cidades.sort(key=lambda x: x[1])
            return lista_cidades[:n]
        except FileNotFoundError:
            print("Arquivo moedas.json não encontrado!")
            return lista_cidades
        
    def converter_moeda_gps(self):
        nome_cidade=str(input("Digite o nome da sua cidade:\n"))
        geolocalizador=Nominatim(user_agent="Generico")
        valor_bruto = int(input("Digite o valor inicial para ser convertido:\n"))
        local=geolocalizador.geocode(nome_cidade)
        lista_moeda=self.moeda_cidade((local.latitude,local.longitude))
        for sigla,km in lista_moeda:
            nome,sigla = MoedaModel.busca_nome_moeda_sigla(sigla)
            sigla=str(sigla)
            sigla=sigla.strip("[]'")
            valor_final=valor_bruto*self.taxas[sigla]
            print(f"{nome} ({sigla}): {valor_final}")
            

    def atualizar_taxas(self):
        print("atualizando taxas...")
        taxas_dados = TaxaModel.obter_taxas(self.api_key)
        if taxas_dados is None:
            print("Erro ao buscar dados da API.")
            return
        self.taxas = taxas_dados["conversion_rates"]

    def consulta_taxas(self):
        return self.taxas