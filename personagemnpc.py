from personagem import Personagem  # Importa a classe Personagem

class PersonagemNPC(Personagem):
    """
    A classe Heroi representa as características de um personagem não jogável no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, frase1, frase2, frase3): # Considerando 3 frases para os NPCs. Podem ser mais
        super().__init__(nome, idade, vida, frase1, frase2, frase3) # O que significa esse "super"?
        

    def conversar(self, personagem):
        """
        Reduz a vida do vilão atacado pelo herói.
        """

    def __str__(self): # Para que o professor deixou isso?
        return f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, Maldade: {self.maldade}'
