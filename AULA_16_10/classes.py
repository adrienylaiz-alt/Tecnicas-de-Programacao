class Pessoa: # Criei o molde para pessoa
    def __init__(self, altura, peso, nome):
        self.nome=nome
        self.altura=altura
        self.peso=peso
    
    def andar(self): #Criamos um comportamento
        print(f"{self.nome}andou 2 passos!") #Acessamos uma propriedade que foi criada

comida = Pessoa(1.60, 70, "Adrieny") #primeiro objeto
pessoa1 = Pessoa(1.70, 80, "João") #segundo objeto
print (comida.nome, comida.altura, comida.peso)
dicionario = [
    {
    "nome_pessoa": comida.nome,
    "peso_pessoa": comida.peso,
    "altura_pessoa": comida.altura
},
    {
    "nome_pessoa": pessoa1.nome,
    "peso_pessoa": pessoa1.peso,
    "altura_pessoa": pessoa1.altura
}
]
for i in range(len(dicionario)):
    print("o nome é:")
    print(dicionario[i]["nome_pessoa"])

    print("o peso é:")
    print(dicionario[i]["peso_pessoa"]) 

    print("a altura é:")
    print(dicionario[i]["altura_pessoa"])
    

