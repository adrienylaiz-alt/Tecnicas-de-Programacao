
class Pessoa: # Crio a classe Pessoa
    def __init__(self, idade, nome): # Recebo a idade e o nome da pessoa
        self.idade = idade # Guardo a idade da pessoa
        self.nome = nome # Guardo o nome da pessoa

    def apresentar(self): # Crio o método para apresentar a pessoa
        return "Meu nome é {} e minha idade é {}.".format(self.nome, self.idade) # Monto a frase colocando o nome e a idade nos espaços reservados


class ArquivoPessoa: # Crio a classe que vai cuidar do arquivo
    def __init__(self, nome_arquivo, tipo_arquivo=".txt"): # Recebo o nome do arquivo e defino o tipo como .txt
        self.nome_arquivo = nome_arquivo # Guardo o nome do arquivo
        self.tipo_arquivo = tipo_arquivo # Guardo o tipo do arquivo

    def exibir(self): # Crio o método para mostrar as informações salvas
        with open(self.nome_arquivo + self.tipo_arquivo, "r", encoding="utf-8") as arquivo: # Abro o arquivo no modo de leitura
            print(arquivo.read()) # Leio e mostro tudo que está salvo no arquivo

    def escrever(self, pessoa, mensagem): # Crio o método para escrever a primeira pessoa e sua mensagem
        with open(self.nome_arquivo + self.tipo_arquivo, "w", encoding="utf-8") as arquivo: # Abro o arquivo no modo de escrita, podendo apagar o conteúdo anterior
            arquivo.write(pessoa.apresentar() + "\n") # Escrevo a apresentação da pessoa e pulo para a próxima linha
            arquivo.write(mensagem + "\n") # Escrevo a mensagem e pulo para a próxima linha

    def adicionar(self, pessoa, mensagem): # Crio o método para adicionar pessoas sem apagar as informações anteriores
        with open(self.nome_arquivo + self.tipo_arquivo, "a", encoding="utf-8") as arquivo: # Abro o arquivo no modo de adicionar informações ao final
            arquivo.write(pessoa.apresentar() + "\n") # Escrevo a apresentação da pessoa e pulo para a próxima linha
            arquivo.write(mensagem + "\n") # Escrevo a mensagem e pulo para a próxima linha


arquivo = ArquivoPessoa("pessoas") # Crio o arquivo pessoas.txt usando a classe ArquivoPessoa

pessoa1 = Pessoa(20, "Adrieny") # Crio a primeira pessoa com idade e nome
pessoa2 = Pessoa(22, "Anelyse") # Crio a segunda pessoa
pessoa3 = Pessoa(19, "Milene") # Crio a terceira pessoa
pessoa4 = Pessoa(21, "Danieli") # Crio a quarta pessoa
pessoa5 = Pessoa(25, "Lorena") # Crio a quinta pessoa
pessoa6 = Pessoa(30, "Heloisa") # Crio a sexta pessoa
pessoa7 = Pessoa(18, "Nicoli") # Crio a sétima pessoa
pessoa8 = Pessoa(24, "Tainara") # Crio a oitava pessoa
pessoa9 = Pessoa(27, "Gabriela") # Crio a nona pessoa
pessoa10 = Pessoa(23, "Biatrys") # Crio a décima pessoa

arquivo.escrever(pessoa1, "Formada e Ciencias COntábeis e Recursos Humanos.") # Escrevo a primeira pessoa e sua mensagem no arquivo
arquivo.adicionar(pessoa2, "Gosto de ler livros e servir nos acampamentos") # Adiciono a segunda pessoa sem apagar a anterior
arquivo.adicionar(pessoa3, "Jogo volei, quando não estou lesionada(estou sempre lesionada)") # Adiciono a terceira pessoa
arquivo.adicionar(pessoa4, "Formada em Arquitetura e Urbanismo e amo viajar") # Adiciono a quarta pessoa
arquivo.adicionar(pessoa5, "Gosto de atuar na area de fisioterapia") # Adiciono a quinta pessoa
arquivo.adicionar(pessoa6, "Sou sofredora do são paulo e orfã do RBD") # Adiciono a sexta pessoa
arquivo.adicionar(pessoa7, "Gosto de matematica e tirar tarot") # Adiciono a sétima pessoa
arquivo.adicionar(pessoa8, "Gosto de ficar por dentro das fofocas(sou psicologa)") # Adiciono a oitava pessoa
arquivo.adicionar(pessoa9, "Jogo futsal e pareço a boneca barbie profissões") # Adiciono a nona pessoa
arquivo.adicionar(pessoa10, "Fã de harry potter e amo cozinhar") # Adiciono a décima pessoa

arquivo.exibir() # Abro o arquivo para ler e mostrar todas as informações salvas
