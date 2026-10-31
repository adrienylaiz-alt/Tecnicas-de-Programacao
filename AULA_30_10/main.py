
class Viveiro:
    viveiro_verde = "Viveiro Verde"

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def valor_total(self):
        return self.preco * self.quantidade

    def exibir(self):
        total = self.valor_total()
        print(f"Nome: {self.nome} | Preço: {self.preco} | Quantidade: {self.quantidade} | Valor Total: {total}")


def calcular_total(plantas):
    total = 0
    for planta in plantas:
        total += planta.valor_total()
    return total


plantas = []

samambaia = Viveiro("Samambaia", 22.9, 5)
samambaia.exibir()
n = int(input("Digite o número de plantas: "))

for i in range(n):
    nome = input(f"Digite o nome da planta {i+1}: ")
    preco = float(input(f"Digite o preço da planta {i+1}: "))
    quantidade = int(input(f"Digite a quantidade da planta {i+1}: "))
    planta = Viveiro(nome, preco, quantidade)
    plantas.append(planta)


for planta in plantas:
    planta.exibir()

total = calcular_total(plantas)
print("Valor total das plantas: R$ {:.2f}".format(total))


with open("plantas.txt", "w", encoding="utf-8") as arq:
    for planta in plantas:
        arq.write(f"{planta.nome};{planta.preco:.2f};{planta.quantidade}")

with open("plantas.txt", "a", encoding="utf-8") as arq:
    arq.write(f"Total: {calcular_total(plantas):.2f}")

with open("plantas.txt", "r", encoding="utf-8") as arq:
    conteudo = arq.read()
    print(conteudo)
