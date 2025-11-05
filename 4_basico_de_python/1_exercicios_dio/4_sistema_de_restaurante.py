from decimal import Decimal, getcontext

# Ajuste de precisão (suficiente para somas de preços)
getcontext().prec = 28


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, preco):
        """Recebe um Decimal representando o preço e adiciona à lista."""
        self.itens.append(preco)

    def calcular_total(self):
        """Retorna a soma de todos os preços como Decimal."""
        return sum(self.itens, Decimal("0.00"))


# Leitura da quantidade de itens
quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    # separa o nome (pode ter espaços) e o preço (último token)
    nome, preco_str = entrada.rsplit(" ", 1)
    # aceita tanto '12.50' quanto '12,50'
    preco_str = preco_str.replace(",", ".")
    pedido.adicionar_item(Decimal(preco_str))

# Exibe o total formatado com duas casas decimais
total = pedido.calcular_total()
print(f"{total:.2f}")
