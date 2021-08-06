import pygame
import config
from player import Player
import player
from game_state import GameState
import missilcoords
import random
gameActive = True
gameStart = False
counter = 0
runOnce = 0
animationTimer = 0
mute = 1

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []

    def set_up(self):

        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print("do set up")
        self.game_state = GameState.RUNNING

        self.load_map("01")


    def update(self):
        if gameStart == False:
            self.handle_events()
            self.render_map(self.screen)
            self.start_screen(self.screen)
        elif gameStart == True:
            self.screen.fill(config.BLACK)

            if gameActive == True:
                self.player.gravity()
                print("update")
                player.playerAnimation = True

            elif gameActive == False:
                print('you lose')

            self.handle_events()
            self.render_map(self.screen)
            self.missile_enc(self.screen)
            self.scoreboard(self.screen)

        for object in self.objects:
            object.render(self.screen)

    def start_screen(self,screen):
        global mute
        self.background = pygame.image.load('imgs/startbackground.png')
        self.background = pygame.transform.scale(self.background,(config.SCREEN_WIDTH,config.SCREEN_HEIGHT))
        screen.blit(self.background, (0,0))

        #Sound
        if mute > 0:
            self.mutebutton = pygame.image.load('imgs/unmute.png')
            pygame.mixer.init()
            pygame.mixer.music.load('aud/backgroundmusic.ogg')
            pygame.mixer.music.play(-1)
        elif mute < 0:
            self.mutebutton = pygame.image.load('imgs/mute.png')
            pygame.mixer.init()
            pygame.mixer.music.unload()

        self.mutebutton = pygame.transform.scale(self.mutebutton,(78,78))
        screen.blit(self.mutebutton,(550,430))


        #Start
        self.startbutton = pygame.image.load('imgs/startbutton.png')
        self.startbutton = pygame.transform.scale(self.startbutton,(192,78))
        screen.blit(self.startbutton,(226,200))
        self.player.playery = 0
        self.player.playerx = 11

    def missile_enc(self, screen):
        global gameActive
        global counter
        increaseDiff = 30

        self.nm1 = pygame.image.load('imgs/n-missle.png')
        self.nm1 = pygame.transform.scale(self.nm1, (config.MISSILESCALE*2,config.MISSILESCALE))
        self.hitbox1 = pygame.Rect(missilcoords.nm1x,missilcoords.nm1y,config.MISSILESCALE*2,config.MISSILESCALE/2)
        screen.blit(self.nm1, self.hitbox1)
        if gameActive == True:
            missilcoords.nm1x += missilcoords.easyvel
            if missilcoords.nm1x > 680:
                missilcoords.nm1x = -150
                missilcoords.nm1y = random.randint(3,278)
        elif gameActive == False:
            missilcoords.nm1x = missilcoords.nm1x

        self.nm2 = pygame.image.load('imgs/n-missle.png')
        self.nm2 = pygame.transform.scale(self.nm2, (config.MISSILESCALE*2, config.MISSILESCALE))
        self.hitbox2 = pygame.Rect(missilcoords.nm2x, missilcoords.nm2y, config.MISSILESCALE * 2, config.MISSILESCALE/2)
        screen.blit(self.nm2, self.hitbox2)
        if gameActive == True:
            missilcoords.nm2x += missilcoords.mediumvel
            if missilcoords.nm2x > 680:
                missilcoords.nm2x = -200
                missilcoords.nm2y = random.randint(270,400)
        elif gameActive == False:
            missilcoords.nm2x = missilcoords.nm2x

        self.nm3 = pygame.image.load('imgs/n-missle.png')
        self.nm3 = pygame.transform.scale(self.nm3, (config.MISSILESCALE * 2, config.MISSILESCALE))
        self.hitbox3 = pygame.Rect(missilcoords.nm3x, missilcoords.nm3y, config.MISSILESCALE * 2, config.MISSILESCALE/2)
        screen.blit(self.nm3, self.hitbox3)
        if gameActive == True:
            missilcoords.nm3x += missilcoords.easyvel
            if missilcoords.nm3x > 680:
                missilcoords.nm3x = -50
                missilcoords.nm3y = random.randint(370,460)
        elif gameActive == False:
            missilcoords.nm3x = missilcoords.nm3x

        self.tm1 = pygame.image.load('imgs/t-missile.png')
        self.tm1 = pygame.transform.scale(self.tm1, (config.MISSILESCALE * 3, config.MISSILESCALE))
        self.hitboxT1 = pygame.Rect(missilcoords.tm1x, missilcoords.tm1y, config.MISSILESCALE * 3, config.MISSILESCALE/2)
        screen.blit(self.tm1, self.hitboxT1)
        if gameActive == True:
            missilcoords.tm1x += missilcoords.hardvel
            if missilcoords.tm1x > 680:
                missilcoords.tm1x = -1700
                missilcoords.tm1y = random.randint(80, 338)
        elif gameActive == False:
            missilcoords.tm1x = missilcoords.tm1x

        self.dm1 = pygame.image.load('imgs/d-missile.png')
        self.dm1 = pygame.transform.scale(self.dm1, (config.MISSILESCALE*2, config.MISSILESCALE))
        self.hitboxD1 = pygame.Rect(missilcoords.dm1x, missilcoords.dm1y, config.MISSILESCALE*2,
                                    config.MISSILESCALE / 2)
        screen.blit(self.dm1, self.hitboxD1)
        if gameActive == True:
            missilcoords.dm1x += missilcoords.dartvel
            if missilcoords.dm1x > 680:
                missilcoords.dm1x = -700
                missilcoords.dm1y = random.randint(3, 100)
        elif gameActive == False:
            missilcoords.dm1x = missilcoords.dm1x


        self.dm2 = pygame.image.load('imgs/d-missile.png')
        self.dm2 = pygame.transform.scale(self.dm2, (config.MISSILESCALE * 2, config.MISSILESCALE))
        self.hitboxD2 = pygame.Rect(missilcoords.dm2x, missilcoords.dm2y, config.MISSILESCALE * 2,
                                    config.MISSILESCALE / 2)
        screen.blit(self.dm2, self.hitboxD2)
        if gameActive == True:
            missilcoords.dm2x += missilcoords.dartvel
            if missilcoords.dm2x > 680:
                missilcoords.dm2x = -700
                missilcoords.dm2y = random.randint(300, 418)
        elif gameActive == False:
            missilcoords.dm2x = missilcoords.dm2x


        self.nm4 = pygame.image.load('imgs/n-missle.png')
        self.nm4 = pygame.transform.scale(self.nm4, (config.MISSILESCALE * 2, config.MISSILESCALE))
        self.hitbox4 = pygame.Rect(missilcoords.nm4x, missilcoords.nm4y, config.MISSILESCALE * 2,
                                   config.MISSILESCALE / 2)
        screen.blit(self.nm4, self.hitbox4)
        if gameActive == True and counter > increaseDiff:
            missilcoords.nm4x += missilcoords.easyvel
            if missilcoords.nm4x > 680:
                missilcoords.nm4x = -150
                missilcoords.nm4y = random.randint(3, 178)
        elif gameActive == False and counter < increaseDiff:
            missilcoords.nm4x = missilcoords.nm4x

        self.nm5 = pygame.image.load('imgs/n-missle.png')
        self.nm5 = pygame.transform.scale(self.nm5, (config.MISSILESCALE * 2, config.MISSILESCALE))
        self.hitbox5 = pygame.Rect(missilcoords.nm5x, missilcoords.nm5y, config.MISSILESCALE * 2,
                                   config.MISSILESCALE / 2)
        screen.blit(self.nm5, self.hitbox5)
        if gameActive == True and counter > increaseDiff:
            missilcoords.nm5x += missilcoords.easyvel
            if missilcoords.nm5x > 680:
                missilcoords.nm5x = -150
                missilcoords.nm5y = random.randint(50, 278)
        elif gameActive == False and counter < increaseDiff:
            missilcoords.nm5x = missilcoords.nm5x



        checkcoords = [self.hitbox1,self.hitbox2,self.hitbox3,self.hitboxT1,self.hitboxD1,self.hitboxD2,
                       self.hitbox4, self.hitbox5]

        ifCollide = self.player.rect.collidelist(checkcoords)

        if ifCollide != -1 or self.player.playery > 9.2:
            self.lose_screen(self.screen)
            gameActive = False


    def scoreboard(self,screen):
        global counter
        if gameActive == True:
            self.font = pygame.font.Font('imgs/font copy.ttf',32)
            counter += 0.02
            textcounter = str(int(counter))
            self.score = self.font.render(textcounter, True, config.WHITE)
        elif gameActive == False:
            counter = counter
        screen.blit(self.score, (10, 3))


    def lose_screen(self, screen):
        global counter
        self.explosion_animation(self.screen)

        self.background = pygame.image.load('imgs/startbackground.png')
        self.background = pygame.transform.scale(self.background, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        screen.blit(self.background, (0, 0))
        self.startbutton = pygame.image.load('imgs/restartbutton.png')
        self.startbutton = pygame.transform.scale(self.startbutton, (190, 98))
        screen.blit(self.startbutton, (226, 200))
        self.font = pygame.font.Font('imgs/font copy.ttf', 48)
        self.deathmessage = 'You Died'
        self.deathmessage = self.font.render(self.deathmessage, True, config.WHITE)
        screen.blit(self.deathmessage,(270,20))

        self.font = pygame.font.Font('imgs/font copy.ttf', 32)
        self.scoremessage = (str(int(counter)))
        self.scoremessage = self.font.render(self.scoremessage, True, config.WHITE)
        self.scoremessage1 = 'Score '
        self.scoremessage1 = self.font.render(self.scoremessage1, True, config.WHITE)
        screen.blit(self.scoremessage, (357, 88))
        screen.blit(self.scoremessage1, (287, 88))

        player.playerAnimation = False
        pygame.mixer.music.unload()



    def explosion_animation(self, screen):
        global animationTimer
        animationTimer += 10
        if animationTimer > 0 and animationTimer < 20:
            self.player.image = pygame.image.load('imgs/e1.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)

            #play explosion sound
            explosionsound = pygame.mixer.Sound('aud/explosionsound.ogg')
            pygame.mixer.Sound.play(explosionsound)
        elif animationTimer > 20 and animationTimer < 40:
            self.player.image = pygame.image.load('imgs/e2.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)
        elif animationTimer > 40 and animationTimer < 60:
            self.player.image = pygame.image.load('imgs/e3.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)
        elif animationTimer > 40 and animationTimer < 60:
            self.player.image = pygame.image.load('imgs/e4.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)
        elif animationTimer > 60 and animationTimer < 80:
            self.player.image = pygame.image.load('imgs/e5.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)
        elif animationTimer > 80 and animationTimer < 100:
            self.player.image = pygame.image.load('imgs/e6.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)
        elif animationTimer > 100 and animationTimer < 120:
            self.player.image = pygame.image.load('imgs/e7.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)
        elif animationTimer > 120 and animationTimer < 140:
            self.player.image = pygame.image.load('imgs/e8.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)
        elif animationTimer > 140:
            self.player.image = pygame.image.load('imgs/blank.png')
            self.player.image = pygame.transform.scale(self.player.image, (64, 64))
            screen.blit(self.player.image, self.player.rect)







    def handle_events(self):
        global jump
        global gameStart
        global gameActive
        global counter
        global runOnce
        global animationTimer
        global mute

        for event in pygame.event.get():
            pygame.key.set_repeat(1,20)
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            #handle Mouse
            elif event.type == pygame.MOUSEBUTTONDOWN and gameActive == True:
                self.rect = pygame.Rect(226, 200, 192, 78)
                self.mute = pygame.Rect(550, 430, 78, 78)
                self.pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(self.pos):
                    gameStart = True
                    animationTimer = 0
                elif self.mute.collidepoint(self.pos):
                    mute = mute * -1
                else:
                    gameStart = False
            elif event.type == pygame.MOUSEBUTTONDOWN and gameActive == False:
                self.rect = pygame.Rect(226, 200, 192, 78)
                self.pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(self.pos):
                    gameActive = True
                    gameStart = False
                    missilcoords.dm1x = -1000
                    missilcoords.dm2x = -2700
                    missilcoords.tm1x = -500
                    missilcoords.nm5x = -150
                    missilcoords.nm4x = -100
                    missilcoords.nm3x = -120
                    missilcoords.nm2x = -150
                    missilcoords.nm1x = -100
                    self.player.playery = 0
                    self.player.playerx = 11
                    self.player.image = pygame.image.load('imgs/player1.png')
                    self.player.image = pygame.transform.scale(self.player.image, (config.SCALE, config.SCALE))
                    counter = 0

            #     handle key
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    runOnce = 0
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.stop_walking()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.stop_walking()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_SPACE: # up
                    runOnce += 1
                    if runOnce == 1:
                        self.player.update_position()

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.player.movef()
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.player.moveb()


    def load_map(self, file_name):
        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
            print(self.map)

    def render_map(self, screen):

        #Map
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

        #Clouds
        global gameStart
        global gameActive

        self.cloud = pygame.image.load('imgs/cloud1.png')
        self.cloud = pygame.transform.scale(self.cloud,(132,48))
        screen.blit(self.cloud,(missilcoords.cloud1x,missilcoords.cloud1y))
        if missilcoords.cloud1x > 720:
            missilcoords.cloud1x = - 150
        else:
            if gameStart and gameActive:
                missilcoords.cloud1x += 1
            elif not gameStart:
                missilcoords.cloud1x = missilcoords.cloud1x


        self.cloud = pygame.image.load('imgs/cloud1.png')
        self.cloud = pygame.transform.scale(self.cloud, (132, 48))
        screen.blit(self.cloud, (missilcoords.cloud2x, missilcoords.cloud2y))
        if missilcoords.cloud2x > 720:
            missilcoords.cloud2x = - 150
        else:
            if gameStart and gameActive:
                missilcoords.cloud2x += 1
            elif not gameStart:
                missilcoords.cloud2x = missilcoords.cloud2x

        self.cloud = pygame.image.load('imgs/cloud2.png')
        self.cloud = pygame.transform.scale(self.cloud, (128, 60))
        screen.blit(self.cloud, (missilcoords.cloud3x, missilcoords.cloud3y))
        if missilcoords.cloud3x > 720:
            missilcoords.cloud3x = - 150
        else:
            if gameStart and gameActive:
                missilcoords.cloud3x += 1
            elif not gameStart:
                missilcoords.cloud3x = missilcoords.cloud3x

        self.cloud = pygame.image.load('imgs/cloud2.png')
        self.cloud = pygame.transform.scale(self.cloud, (88, 20))
        screen.blit(self.cloud, (missilcoords.cloud4x, missilcoords.cloud4y))
        if missilcoords.cloud4x > 720:
            missilcoords.cloud4x = - 150
        else:
            if gameStart and gameActive:
                missilcoords.cloud4x += 1
            elif not gameStart:
                missilcoords.cloud4x = missilcoords.cloud4x

        self.cloud = pygame.image.load('imgs/cloud2.png')
        self.cloud = pygame.transform.scale(self.cloud, (88, 20))
        screen.blit(self.cloud, (missilcoords.cloud5x, missilcoords.cloud5y))
        if missilcoords.cloud5x > 720:
            missilcoords.cloud5x = - 150
        else:
            if gameStart and gameActive:
                missilcoords.cloud5x += 1
            elif not gameStart:
                missilcoords.cloud5x = missilcoords.cloud5x

map_tile_image = {
    "G" : pygame.transform.scale(pygame.image.load("imgs/sky.png"), (config.SCALE, config.SCALE)),
    "D": pygame.transform.scale(pygame.image.load('imgs/ground.png'), (config.SCALE, config.SCALE))
}
