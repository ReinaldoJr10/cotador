import requests

class TaxaModel:
    def __init__(self, sigla, taxa):
        self.sigla = sigla
        self.taxa = taxa

    @staticmethod
    def obter_taxas(api_key):
        url_requisicao = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        try:
            requisicao = requests.get(url_requisicao)
            requisicao.raise_for_status()
            return requisicao.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a API: {e}")
            return None

