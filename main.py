import pygame, random
from pygame.math import Vector2

WHITE = (255,255,255)
RED = (255, 0, 0)
FPS = 30
NUMBER_OF_ANTS = 10



class Ant(object):
    def __init__(self, app):
        self.app = app
        self.image = pygame.image.load('./res/ant.png')
        self.rect = self.image.get_rect()
        self.position = self.x, self.y = random.randint(0, self.app.width - self.rect.width), \
            random.randint(0, self.app.height - self.rect.height)
        self.position = Vector2(random.randint(0, self.app.width - self.rect.width), \
            random.randint(0, self.app.height - self.rect.height))
        self.direction = self.up, self.fwd = True, True
        self.speed = 3

    def show(self):
        self.app._display_surf.blit(self.image, self.position)

    def go_to_destination_point(self):
        #self.angle = self.position.angle_to(self.app.ants_destination_point)

        self.position += (self.app.ants_destination_point-self.position).normalize()*self.speed





        print()

    # def move(self):
    #
    #     if self.x == 1:
    #         self.up = False
    #     elif self.x == self.app.width - self.rect.width:
    #         self.up = True
    #
    #     if self.y == 1:
    #         self.fwd = False
    #     elif self.y == self.app.height - self.rect.height:
    #         self.fwd = True
    #
    #     if self.up:
    #         self.x -= 1
    #     else:
    #         self.x += 1
    #
    #     if self.fwd:
    #         self.y -= 1
    #     else:
    #         self.y += 1
    #
    #     self.position = self.x, self.y


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 800, 600
        self.app_logo = './res/logo.png'
        self.app_title = 'Ant\'s pathfinding'
        self.clock = pygame.time.Clock()


        self.ants = [Ant(self) for i in range(NUMBER_OF_ANTS)]
        self.ants_destination_point = (random.randint(0,self.width),\
                                       random.randint(0, self.height))

    def on_init(self):
        pygame.init()
        logo = pygame.image.load(self.app_logo)
        pygame.display.set_icon(logo)
        pygame.display.set_caption(self.app_title)
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.MOUSEMOTION:
            self.ants_destination_point = pygame.mouse.get_pos()


    def on_loop(self):
        for ant in self.ants:
            ant.go_to_destination_point()


    def on_render(self):
        self._display_surf.fill(WHITE)
        pygame.draw.circle(self._display_surf, RED, self.ants_destination_point, 20)
        for ant in self.ants:
            ant.show()
        pygame.display.flip()


    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == '__main__':
    theApp = App()
    theApp.on_execute()
