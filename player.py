import pygame
import config
vel = 0.08
jump = False
counter = 0
playerAnimation = True
walking = False


class Player:
    def __init__(self, x, y):

        print("player created")
        self.playerx = 11
        self.playery = 0
        self.image = pygame.image.load('imgs/player1.png')
        self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))
        self.rect = pygame.Rect(self.playerx * config.SCALE, self.playery * config.SCALE,
                                config.SCALE, config.SCALE)

    def update(self):
        print("player updated")


    def update_position(self):
        #change vertical acceleration (up or down)
        global vel
        vel = vel *-1



    def movef(self):
        #moving forwards
        global playerAnimation
        global walking
        if self.playerx < 0.2:
            return
        elif playerAnimation == True:
            time = 70 / 70000
            vel = time * config.SPEED

            self.playerx -= vel
            self.rect = pygame.Rect(self.playerx * config.SCALE, self.playery * config.SCALE,
                                    config.SCALE, config.SCALE)
            walking = True
        else:
            print('gameover')

    def moveb(self):
        #moving backwards
        global playerAnimation
        global walking
        if self.playerx > 12:
            return
        elif playerAnimation == True:
            time = 70 / 70000
            vel = time * config.SPEED

            self.playerx += vel
            self.rect = pygame.Rect(self.playerx * config.SCALE, self.playery * config.SCALE,
                                    config.SCALE, config.SCALE)

            walking = True
        else:
            print('gameover')

    def stop_walking(self):
        global walking
        walking = False


    def gravity(self):
        global vel
        if self.playery < 0:
            self.playery = 0
        else:
            self.playery += vel
            self.rect = pygame.Rect(self.playerx * config.SCALE, self.playery * config.SCALE,
                                        config.SCALE, config.SCALE)


    def render(self, screen):
        global counter
        global playerAnimation
        counter = counter + 3.7
        if playerAnimation == True:
            #animating player avatar frame by frame
            if counter < 60 and counter > 30:
                self.image = pygame.image.load('imgs/player1.png')
                self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))

            elif counter >=60 and counter < 90:
                if not walking:
                    self.image = pygame.image.load('imgs/player3.png')
                elif walking:
                    self.image=pygame.image.load('imgs/player3walk.png')
                self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))

            elif counter >= 90 and counter <120:
                if not walking:
                    self.image = pygame.image.load('imgs/player2.png')
                elif walking:
                    self.image = pygame.image.load('imgs/player2walk.png')
                self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))

            elif counter > 120:
                if not walking:
                    self.image = pygame.image.load('imgs/player3.png')
                elif walking:
                    self.image = pygame.image.load('imgs/player3walk.png')
                self.image = pygame.transform.scale(self.image, (config.SCALE, config.SCALE))

                counter = 0
        elif playerAnimation == False:
            print('gameover')


        screen.blit(self.image,self.rect)
