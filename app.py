import pygame
from pygame import mixer

screen = pygame.display.set_mode((800, 600))
pygame.init()


class Enemy:

    def covid(self):
        pass

    def alien(self):
        pass

class Player:

    def __init__(self):
        self.x = 370
        self.y = 480

    def move(self, xChange):
        self.x -= xChange
        print(self.x)


class Spaceship(Player):

    def show(self, x, y=480):
        self.image = pygame.image.load('spaceship.png')
        screen.blit(self.image, (x, y))


class Stats:

    def score(self):
        pass

    def kills(self):
        pass


class Game:

    def __init__(self):
        # Intialize the pygame

        # Background
        self.background = pygame.image.load('bk1.jpg')

        # Sound
        mixer.music.load("background.mp3")
        mixer.music.play(-1)

        # Caption and Icon
        pygame.display.set_caption("COVID INVADER")
        self.icon = pygame.image.load('ussf.png')
        pygame.display.set_icon(self.icon)
        self.playerX_change = 0

        self.Player1 = Spaceship()

    def start(self):
        running = True
        x_move = 0
        while running:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_move = -1
                        print("left")
                    if event.key == pygame.K_RIGHT:
                        x_move = 1
                        print("right")
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_move = 0

            self.Player1.x += x_move
            if self.Player1.x >= 736:
                self.Player1.x = 736
            elif self.Player1.x <= 0:
                self.Player1.x = 0

            self.Player1.show(x=self.Player1.x)
            pygame.display.update()






if __name__ == "__main__":
    game = Game()
    game.start()