from personagem import Personagem  # Importa a classe Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, maldade):
        super().__init__(nome, idade, vida)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade

    def ataque(self, personagem):
        """
        Reduz a vida do vilão atacado pelo herói.
        """
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida()

    def subir_nivel(self):
        """
        Aumenta o nível do personagem e outros de seus atibutos particulares como força, vida e habilidade com magia por exemplo
        """

    def __str__(self):
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
