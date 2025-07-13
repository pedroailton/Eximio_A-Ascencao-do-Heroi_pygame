# Classe para rodar o jogo e carregar as imagens da interface:

from settings import *
from support import *
from timer import Timer

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('O Exímio: A Ascenção Do Herói')
        self.clock = pygame.time.Clock()
        self.running = True
        self.import_assets()

        # grupos
        self.all_sprites = pygame.sprite.Group()

        # data
        player_monster_list = ['Espadachim', 'Arqueiro', 'Mago']
        self.player_monsters = [Monster(name, self.back_surfs(name)) for name in player_monster_list]

    def import_assets(self):
        self.back_surfs = folder_importer('images', 'back')
        print(self.back_surfs)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # update
            self.all_sprites.update(dt)

            # draw
            self.all_sprites.draw(self.display_surface)
            pygame.display.update()
        
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()