import json

class Personagem:
    def __init__(self, nome, sexo, animacao, superpoder, tipo, universo, idade, protagonista):
        self.nome = nome
        self.sexo = sexo
        self.animacao = animacao
        self.superpoder = superpoder
        self.tipo = tipo
        self.universo = universo
        self.idade = idade
        self.protagonista = protagonista

    def __repr__(self):
        return self.nome

class Akinator:
    def __init__(self, file):
        self.personagens = self._carregar(file)

    def _carregar(self, file):
        with open(file, 'r') as arquivo:
            dados = json.load(arquivo)
            personagens = []
            for personagem in dados:
                personagens.append(
                    Personagem(personagem["nome"], personagem["sexo"], personagem["animacao"],
                               personagem["superpoder"], personagem["tipo"], personagem["universo"],
                               personagem["idade"], personagem["protagonista"])
                )
            return personagens

    def _pergunta(self, pergunta, caracteristica):
        resposta = input(pergunta + " sim | nao ").lower()
        return resposta == 'sim'

    def jogo(self):
        characters = self.personagens

        perguntas = [
            ("Seu personagem é masculino?", "sexo", "masculino"),
            ("Seu personagem é de uma animação?", "animacao", True),
            ("Seu personagem tem superpoder?", "superpoder", True),
            ("Seu personagem é um herói?", "tipo", "herói"),
            ("Seu personagem é o protagonista?", "protagonista", True)
        ]

        for pergunta, caracteristica, valor in perguntas:
            resposta = self._pergunta(pergunta, caracteristica)
            characters = [personagem for personagem in characters if getattr(personagem, caracteristica) == valor] if resposta else [personagem for personagem in characters if getattr(personagem, caracteristica) != valor]

            if len(characters) == 1:
                print(f"Acho que o personagem é {characters[0].nome}!")
                return
            elif len(characters) == 0:
                print("Não consegui adivinhar o personagem.")
                return

game = Akinator("personagens.json")
game.jogo()