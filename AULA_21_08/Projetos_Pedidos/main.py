from Projeto_Pedidos.pedidos import cadastrar_cliente
from Projeto_Pedidos.pedidos import cadastrar_produtos
from Projeto_Pedidos.pedidos import calcular_total
from Projeto_Pedidos.pedidos import emitir_recibo
from Projeto_Pedidos.somar_itens import somar_itens
from Projeto_Pedidos.descricao_pedido import descrever_pedido

try:
    cliente = cadastrar_cliente()
    produtos = cadastrar_produtos()
    valores = [p["valor"] for p in produtos]
    subtotal, total = calcular_total(valores)
    emitir_recibo(cliente, produtos, subtotal, total)
    dados = {
        "observacao": "Sem cebola",
        "retirada": False
    }
    descrever_pedido(cliente["nome"], **dados)
    valores_teste = (10, 20, 30)
    resultado = somar_itens(*valores_teste)
    print(f"Soma dos itens: {resultado}")

except ValueError:
    print("Erro: digite um valor numérico válido para o produto.")

except KeyError:
    print("Erro: alguma informação do cliente ou produto está faltando.")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")