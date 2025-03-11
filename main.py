import os
import asyncio
from controllers.moeda_controller import MoedaController
from views.moeda_view import MoedaView


# Obtém a chave da API
api_key = os.getenv("EXCHANGE_API_KEY")

controller = MoedaController(api_key)

async def main():
    while True:
        opcao = MoedaView.exibir_opcoes()
        if opcao == 1:
            controller.consultar_taxa()
        elif opcao == 2:
            controller.converter_moeda()
        elif opcao == 3:
            controller.converter_moeda_gps()
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        print("Pressione Enter para continuar...")
        input()

if __name__ == "__main__":
    asyncio.run(main())
