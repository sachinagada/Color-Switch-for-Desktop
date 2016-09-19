
import pygame
from math import *
import random


red = (255, 20, 147)
blue = (0, 191 , 255)
white = (255, 165, 0)
green = (0, 255, 0)

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.cx = 200
        self.cy = 550
        self.r = 10
        self.color = random.choice([red,blue,green,white])
        self.thickness = 10
        self.color = random.choice([red,blue,green,white])
        self.rect = pygame.Rect(self.cx - self.r, self.cy - self.r,
                                2 * self.r, 2 * self.r)
        self.image = pygame.Surface((2 * self.r, 2 * self.r),
                                    pygame.SRCALPHA)  # make it transparent
        self.image = self.image.convert_alpha()

    # def draw(self, screen):
    #     pygame.draw.circle(screen, self.color, (self.cx, self.cy), self.r)
    def jump(self):
        self.cy -= 25
        self.rect = pygame.Rect(self.cx - self.r, self.cy - self.r, 2*self.r, 2*self.r)

    def update(self):
        if self.cy==(600-self.r):
            self.cy=600-self.r
        else:
            self.cy+=1
        self.rect = pygame.Rect(self.cx - self.r, self.cy - self.r,
                                2 * self.r, 2 * self.r)
        pygame.draw.circle(self.image, self.color, 
                          (self.r, self.r), self.r)

class ColorChanger(pygame.sprite.Sprite):
    def __init__(self,x,y,ball):
        super(ColorChanger, self).__init__()
        self.cx = x
        self.cy = y
        self.s = 10
        self.ball=ball
        self.rect = pygame.Rect(self.cx - self.s, self.cy - self.s,
                        2 * self.s, 2 * self.s)
        self.image = pygame.Surface((2 * self.s, 2 * self.s),
                                    pygame.SRCALPHA)  # make it transparent
        self.image = self.image.convert_alpha()

        # pygame.draw.rect(self.image, red, (0, 0, self.s, self.s), 0)
        # pygame.draw.rect(self.image, green, (self.s, 0, self.s, self.s), 0)
        # pygame.draw.rect(self.image, blue, (0, self.s, self.s,self.s), 0)
        # pygame.draw.rect(self.image, white, (self.s, self.s,self.s,self.s), 0)


    def update(self):
        #for ball in PygameGame.ball:
        
        self.rect = pygame.Rect(self.cx - self.s, self.cy - self.s,
                            2 * self.s, 2 * self.s)
        pygame.draw.rect(self.image, red, (0, 0, self.s, self.s), 0)
        pygame.draw.rect(self.image, green, (self.s, 0, self.s, self.s), 0)
        pygame.draw.rect(self.image, blue, (0, self.s, self.s,self.s), 0)
        pygame.draw.rect(self.image, white, (self.s, self.s,self.s,self.s), 0)   

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacles, self).__init__()
        self.cx = None
        self.cy = None
        self.color = None


class RegularObs(Obstacles):
    def __init__(self,ball, cy=100):
        super().__init__()
        self. cx = 150
        self.cy = cy
        self.speed=128
        self.anglechange = pi/self.speed
        self.anglestart= 0
        self.angleend = self.anglestart + pi/2
        self.thickness = 10
        self.d=100

        self.ball=ball
        self.rect = pygame.Rect(self.cx - self.d, self.cy - self.d,
                                2 * self.d, 2 * self.d)
        self.image = pygame.Surface((2 * self.d, 2 * self.d),
                                    pygame.SRCALPHA)  # make it transparent
        self.image = self.image.convert_alpha()

    def update(self):
        self.anglechange = pi/self.speed
        self.anglestart+=self.anglechange
        self.image.fill((0,0,0,0))
        #for ball in PygameGame.ball:
        
        self.rect = pygame.Rect(self.cx - self.d, self.cy - self.d,
                                2 * self.d, 2 * self.d)
        pygame.draw.arc(self.image, red, (self.d, self.d,100,100), self.anglestart, self.anglestart+ pi/2, self.thickness)
        pygame.draw.arc(self.image, blue, (self.d, self.d,100,100), self.anglestart+ pi/2, self.anglestart + pi, self.thickness)
        pygame.draw.arc(self.image, white, (self.d, self.d,100,100), self.anglestart + pi, self.anglestart + 3*pi/2, self.thickness)
        pygame.draw.arc(self.image, green, (self.d, self.d,100,100), self.anglestart + 3*pi/2, self.anglestart + 2*pi, self.thickness) 

def collisionRegularObs(ball,obj):
    if obj.anglestart % (2*pi) <= pi/2 and obj.anglestart % (2*pi) >= 0:
       bottomcollisionColor = white
       topcollisionColor = red
    elif obj.anglestart % (2*pi) >= pi/2 and obj.anglestart % (2*pi) <= pi:
        bottomcollisionColor = blue
        topcollisionColor = green
    elif obj.anglestart % (2*pi) >= pi and obj.anglestart % (2*pi) <= 3*pi/2:
        bottomcollisionColor = red
        topcollisionColor = white
    elif obj.anglestart % (2*pi) >= 3*pi/2 and obj.anglestart % (2*pi) <= 2*pi:
        bottomcollisionColor = green
        topcollisionColor = blue
    obstacleEntryX = obj.cx + 50
    obstacleEntryY1 = obj.cy + 100
    obstacleEntryY2 = obj.cy 
    # print(obstacleEntryY1, obstacleEntryY2, obstacleEntryX)
    if (abs(ball.cy-obstacleEntryY1) <= ball.r and ball.color!=bottomcollisionColor): 
        return True
    elif (abs(ball.cy-obstacleEntryY2) <= ball.r and ball.color!=topcollisionColor):
        return True
    return False


class PygameGame(object):

    def init(self):
        self.GameOver=False
        self.score=0

        self.b=Ball()
        self.ball=pygame.sprite.Group(self.b)

        self.c=ColorChanger(200,150,self.ball)
        self.colorChanger=pygame.sprite.Group(self.c)

        self.c3 = ColorChanger(200, 350,self.ball)
        self.colorChanger.add(self.c3)

        self.rOs = RegularObs(self.ball,200)
        self.rOs1 = RegularObs(self.ball,400)
        self.regularObs=pygame.sprite.Group(self.rOs1,self.rOs)

        self.addspeed = False


    def mousePressed(self, x, y):
        pass

    def mouseReleased(self, x, y):
        pass

    def mouseMotion(self, x, y):
        pass

    def mouseDrag(self, x, y):
        pass

    def keyPressed(self, keyCode, modifier):
        if self.GameOver == False:
            if keyCode == pygame.K_UP:
                for ball in self.ball:
                    ball.jump()
        else:
            if keyCode == pygame.K_r:
                self.GameOver = False
                for ball in self.ball:
                    ball.cy = 550
                    self.GameOver=False
                self.score=0

                self.b=Ball()
                self.ball=pygame.sprite.Group(self.b)

                self.c=ColorChanger(200,150,self.ball)
                self.colorChanger=pygame.sprite.Group(self.c)

                self.c3 = ColorChanger(200, 350,self.ball)
                self.colorChanger.add(self.c3)

                self.rOs = RegularObs(self.ball,200)
                self.rOs1 = RegularObs(self.ball,400)
                self.regularObs=pygame.sprite.Group(self.rOs1,self.rOs)

                self.addspeed = False
                    



    def keyReleased(self, keyCode, modifier):
        pass

    def timerFired(self, dt):
        self.ball.update()
 
        for ball in self.ball:
            if ball.cy < 130:
                ball.cy = 550
                self.c=ColorChanger(200,150,self.ball)
                self.c3 = ColorChanger(200, 350,self.ball)
                self.colorChanger.add(self.c)
                self.colorChanger.add(self.c3)
        if self.addspeed == True:
            for obstacle in self.regularObs:
                if obstacle.speed > 10:
                    obstacle.speed /=1.3
            self.addspeed = False
        
        self.regularObs.update()
        self.colorChanger.update()

        if pygame.sprite.groupcollide(self.ball, self.colorChanger, False, True, 
            pygame.sprite.collide_rect):
            colorList=[red,blue,green,white]
            for ball in self.ball:
                colorList.remove(ball.color)
                ball.color= random.choice(colorList)
                self.score+=1
                if self.score %2 == 0: 
                    self.addspeed = True

        if pygame.sprite.groupcollide(self.ball, self.regularObs, False, False, 
            collisionRegularObs):
            self.GameOver=True
            # for orb in self.regularObs:
            #     orb.anglestart += orb.anglechange
        # self.XObsClock.anglestart += self.XObsClock.anglechange
        # self.XObsCounter.anglestart += self.XObsCounter.anglechange
        # self.Pinwheel.anglestart += self.Pinwheel.anglechange
        #self.regularObs.collision(self.ball) #CORRECT ONE

        self.a = [RegularObs, RegularObs, RegularObs]
        self.obstacleClass = random.choice(self.a)
        self.newObstacle = self.obstacleClass(100)

        # if len(self.currObstacle) < 3:
        #     self.currObstacle.append(self.newObstacle)

    def redrawAll(self, screen):
        if self.GameOver == False:
            self.ball.draw(screen)
            self.colorChanger.draw(screen)
            # self.regularObs.draw(screen)
            self.regularObs.draw(screen)
            # self.regularObs1.draw(screen)
            # self.regularObs2.draw(screen)

            
            myfont = pygame.font.SysFont("comicsansms",20)
            label = myfont.render("Score: " + str(self.score), 1,(255,255,0))
            screen.blit(label,(20,20))
        else:
            gameOverScreen = pygame.display.set_mode((400, 600))
            myfont = pygame.font.SysFont("comicsansms", 48)
            label = myfont.render("LOSER", 1, (255,255,0))
            myfont1 = pygame.font.SysFont("comicsansms", 24)
            label2 = myfont1.render("Play Again?", 1, (255, 255, 0))
            label3 = myfont1.render("Press 'r' to restart", 1, (255, 255, 0))
            label4 = myfont.render("Score: " + str(self.score), 1, (255, 255,0))
            screen.blit(label, (120, 100))
            screen.blit(label2, (140, 250))
            screen.blit(label3, (100, 290))
            screen.blit(label4, (100, 380))



        #self.Pinwheel.draw(screen)

    def isKeyPressed(self, key):
        ''' return whether a specific key is being held '''
        return self._keys.get(key, False)

    def __init__(self, width=400, height=600, fps=50, title="112 Pygame Game"):
        self.width = width
        self.height = height
        self.fps = fps
        self.title = title
        self.bgColor = (0, 0, 0)
        pygame.init()

    def run(self):

        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((self.width, self.height))
        # set the title of the window
        pygame.display.set_caption(self.title)

        # stores all the keys currently being held down
        self._keys = dict()

        # call game-specific initialization
        self.init()
        pygame.font.init()
        playing = True
        while playing:
            time = clock.tick(self.fps)
            self.timerFired(time)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.mousePressed(*(event.pos))
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    self.mouseReleased(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons == (0, 0, 0)):
                    self.mouseMotion(*(event.pos))
                elif (event.type == pygame.MOUSEMOTION and
                      event.buttons[0] == 1):
                    self.mouseDrag(*(event.pos))
                elif event.type == pygame.KEYDOWN:
                    self._keys[event.key] = True
                    self.keyPressed(event.key, event.mod)
                elif event.type == pygame.KEYUP:
                    self._keys[event.key] = False
                    self.keyReleased(event.key, event.mod)
                elif event.type == pygame.QUIT:
                    playing = False
            screen.fill(self.bgColor)
            self.redrawAll(screen)
            pygame.display.flip()

        pygame.quit()


def main():
    game = PygameGame()
    game.run()

if __name__ == '__main__':
    main()