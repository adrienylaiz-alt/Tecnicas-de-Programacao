
import json
from datetime import date
from pathlib import Path
from models.pessoa import Pessoa


class ErroArquivoPessoa(Exception):
    pass


class ArquivoPessoa:
    def __init__(self, pessoa):
        self.pessoa = pessoa

    def salvar(self):
        try:
            pasta = Path("dados") / date.today().isoformat()
            pasta.mkdir(parents=True, exist_ok=True)

            arquivo = pasta / f"{self.pessoa.nome}.json"

            dados = {
                "nome": self.pessoa.nome,
                "data_nascimento": self.pessoa.data_nascimento.isoformat(),
                "data_atual": self.pessoa.data_atual.isoformat(),
                "idade": self.pessoa.idade
            }

            with open(arquivo, "w", encoding="utf-8") as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)

            return str(arquivo)

        except (OSError, TypeError, ValueError) as erro:
            raise ErroArquivoPessoa("Erro ao salvar os dados da pessoa.") from erro


def processar_pessoas():
    pessoas = [
        Pessoa("Ana", date(2000, 12, 15)),
        Pessoa("Carlos", date(1998, 5, 10))
    ]

    for pessoa in pessoas:
        print(pessoa.apresentar())

        arquivo = ArquivoPessoa(pessoa)

        try:
            caminho = arquivo.salvar()
            print(f"Arquivo salvo em: {caminho}")
        except ErroArquivoPessoa as erro:
            print(erro)
