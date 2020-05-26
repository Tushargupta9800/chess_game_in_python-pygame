import pygame
pygame.init()

win = pygame.display.set_mode((650,650))
pygame.display.set_caption("Shatranj")
menu = pygame.image.load('data/menu.png')
play = pygame.image.load('data/play.png')
exiti = pygame.image.load('data/exit.png')
sraja = pygame.image.load('data/sraja.png')
kraja = pygame.image.load('data/kraja.png')
srani = pygame.image.load('data/srani.png')
krani = pygame.image.load('data/krani.png')
kghodha = pygame.image.load('data/kghodha.png')
sghodha = pygame.image.load('data/sghodha.png')
kooth = pygame.image.load('data/kooth.png')
sooth = pygame.image.load('data/sooth.png')
khaathi = pygame.image.load('data/khaathi.png')
shaathi = pygame.image.load('data/shaathi.png')
spyada = pygame.image.load('data/spyada.png')
kpyada = pygame.image.load('data/kpyada.png')
red = pygame.image.load('data/red.png')
blue = pygame.image.load('data/blue.png')
exitend = pygame.image.load('data/exitend.png')
green = pygame.image.load('data/green.png')
swin = pygame.image.load('data/swin.png')
kwin = pygame.image.load('data/kwin.png')
elenum = [khaathi, kghodha, kooth, kraja, krani, kpyada, shaathi, sghodha, sooth, srani, sraja, spyada]
posx = [62, 130, 197, 264, 330, 397, 463, 529]
posy = [60, 127, 194, 261, 328, 395, 462, 526]

bk = pygame.image.load('data/board.jpg')
run = True
whowin = True

def winner(whowin):
    khatm = True
    while khatm:
        win.blit(bk, (0,0))
        win.blit(exitend, (523, 57))
        if whowin:
            win.blit(swin, (-290, 100))
        else:
            win.blit(kwin, (-290, 100))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if x > 525 and x < 588 and y > 57 and y < 120:
                    pygame.quit()

class simple(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class printele(object):
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.num = num
    def draw(self, win):
        win.blit(elenum[self.num], (posx[self.x],posy[self.y]))

kpiyada1 = printele(0, 1, 5)
kpiyada2 = printele(1, 1, 5)
kpiyada3 = printele(2, 1, 5)
kpiyada4 = printele(3, 1, 5)
kpiyada5 = printele(4, 1, 5)
kpiyada6 = printele(5, 1, 5)
kpiyada7 = printele(6, 1, 5)
kpiyada8 = printele(7, 1, 5)
spiyada1 = printele(0, 6, 11)
spiyada2 = printele(1, 6, 11)
spiyada3 = printele(2, 6, 11)
spiyada4 = printele(3, 6, 11)
spiyada5 = printele(4, 6, 11)
spiyada6 = printele(5, 6, 11)
spiyada7 = printele(6, 6, 11)
spiyada8 = printele(7, 6, 11)
karaja = printele(3, 0, 3)
karani = printele(4, 0, 4)
kahaathi1 = printele(0, 0, 0)
kahaathi2 = printele(7, 0, 0)
kaooth1 = printele(2, 0, 2)
kaooth2 = printele(5, 0, 2)
kaghodha1 = printele(1, 0, 1)
kaghodha2 = printele(6, 0, 1)
saraja = printele(3, 7, 9)
sarani = printele(4, 7, 10)
sahaathi1 = printele(0, 7, 6)
sahaathi2 = printele(7, 7, 6)
saooth1 = printele(2, 7, 8)
saooth2 = printele(5, 7, 8)
saghodha1 = printele(1, 7, 7)
saghodha2 = printele(6, 7, 7)
elementss = [saraja, sarani, saooth1, saghodha1, sahaathi1, saooth2, saghodha2, sahaathi2, spiyada1, spiyada2, spiyada3, spiyada4, spiyada5, spiyada6, spiyada7, spiyada8]
elementsk = [karaja, karani, kaooth1, kaghodha1, kahaathi1, kaooth2, kaghodha2, kahaathi2, kpiyada1, kpiyada2, kpiyada3, kpiyada4, kpiyada5, kpiyada6, kpiyada7, kpiyada8]

def draw():
    win.blit(bk, (0,0))
    for ele in elementss:
        ele.draw(win)
    for ele in elementsk:
        ele.draw(win)
    pygame.display.update()

def game():
    draw()
    possible = []
    forthis = []
    total = 32
    start = True
    safed = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        yess = True
        yesk = True
        
        for i in elementss:
            if i.num == 10:
                yess = False

        for i in elementsk:
            if i.num == 3:
                whowin = False
                yesk = False

        if yess:
            whowin = False
            while yess:
                whowin = False
                winner(whowin)
        if yesk:
            while yesk:
                whowin = True
                winner(whowin)

        if safed:
            wait = True
            while wait:
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        for i in possible:
                            if posx[i.x] - 2 < mx and posx[i.x] + 60 > mx and posy[i.y] - 1 < my and posy[i.y] + 60 > my:
                                safed = False
                                wait = False
                                for j in elementsk:
                                    if j.x == i.x and j.y == i.y:
                                        elementsk.remove(j)
                                        total -= 1
                                forthis[0].x = i.x
                                forthis[0].y = i.y
                                continue
                        possible.clear()
                        forthis.clear()
                        draw()
                        
                        if wait:
                            for blah in elementss:
                                if posx[blah.x] - 2 < mx and posx[blah.x] + 60 > mx and posy[blah.y] - 1 < my and posy[blah.y] + 60 > my:
                                      forthis.append(blah)
                                      win.blit(green, (posx[blah.x]-7, posy[blah.y] - 8))
                                      pygame.display.update()
                                      if blah.num == 9:
                                          rx = blah.x
                                          ry = blah.y
                                          rxm = blah.x
                                          ryp = blah.y
                                          rxp = blah.x
                                          rym = blah.y
                                          will = [0,0,0,0,0,0,0,0]
                                          for i in range(7):
                                              rxm -= 1
                                              rxp += 1
                                              rym -= 1
                                              ryp += 1

                                              isit = [0,0,0,0,0,0,0,0]
                                              for i in elementss:
                                                  if i.x == rxm and i.y == rym and rym >= 0 and rxm >= 0 and will[0] == 0:
                                                      isit[0] = 1
                                                      will[0] = 1
                                                  if i.x == rxp and i.y == rym and rxp <= 7 and rym >= 0 and will[1] == 0:
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rxm and i.y == ryp and ryp <= 7 and rxm >= 0and will[2] == 0:
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxp and i.y == ryp and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                      isit[3] = 1
                                                      will[3] = 1
                                                  if i.x == rx and i.y == rym and rym >= 0 and will[4] == 0:
                                                      isit[4] = 1
                                                      will[4] = 1
                                                  if i.x == rxp and i.y == ry and rxp <= 7 and will[5] == 0:
                                                      isit[5] = 1
                                                      will[5] = 1
                                                  if i.x == rx and i.y == ryp and ryp <= 7 and will[6] == 0:
                                                      isit[6] = 1
                                                      will[6] = 1
                                                  if i.x == rxm and i.y == ry and rxm >= 0 and will[7] == 0:
                                                      isit[7] = 1
                                                      will[7] = 1

                                              for i in elementsk:
                                                  if i.x == rxm and i.y == rym and rym >= 0 and rxm >= 0and will[0] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      will[0] = 1
                                                      isit[0] = 1
                                                  if i.x == rxp and i.y == rym and rxp <= 7 and rym >= 0 and will[1] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rxm and i.y == ryp and ryp <= 7 and rxm >= 0 and will[2] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxp and i.y == ryp and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[3] = 1
                                                      will[3] = 1
                                                  if i.x == rx and i.y == rym and rym >= 0 and will[4] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      will[4] = 1
                                                      isit[4] = 1
                                                  if i.x == rxp and i.y == ry and rxp <= 7 and will[5] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[5] = 1
                                                      will[5] = 1
                                                  if i.x == rx and i.y == ryp and ryp <= 7 and will[6] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[6] = 1
                                                      will[6] = 1
                                                  if i.x == rxm and i.y == ry and rxm >= 0 and will[7] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[7] = 1
                                                      will[7] = 1

                                              if isit[0] == 0 and rym >= 0 and rxm >=0 and will[0] == 0:
                                                  temp = simple(rxm, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[rym] - 8))
                                              if isit[1] == 0 and rxp <= 7 and rym >=0 and will[1] == 0:
                                                  temp = simple(rxp, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[rym] - 8))
                                              if isit[2] == 0 and ryp <= 7 and rxm >=0 and will[2] == 0:
                                                  temp = simple(rxm, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[ryp] - 8))
                                              if isit[3] == 0 and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                  temp = simple(rxp, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[ryp] - 8))
                                              if isit[4] == 0 and rym >= 0 and will[4] == 0:
                                                  temp = simple(rx, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[rym] - 8))
                                              if isit[5] == 0 and rxp <= 7 and will[5] == 0:
                                                  temp = simple(rxp, ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[ry] - 8))
                                              if isit[6] == 0 and ryp <= 7 and will[6] == 0:
                                                  temp = simple(rx, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[ryp] - 8))
                                              if isit[7] == 0 and rxm >= 0 and will[7] == 0:
                                                  temp = simple(rxm, ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[ry] - 8))

                                              pygame.display.update()

                                              
                                      if blah.num == 8:
                                          rxm = blah.x
                                          ryp = blah.y
                                          rxp = blah.x
                                          rym = blah.y
                                          will = [0,0,0,0]
                                          for i in range(7):
                                              rxm -= 1
                                              rxp += 1
                                              rym -= 1
                                              ryp += 1

                                              isit = [0,0,0,0]
                                              for i in elementss:
                                                  if i.x == rxm and i.y == rym and rym >= 0 and rxm >= 0 and will[0] == 0:
                                                      isit[0] = 1
                                                      will[0] = 1
                                                  if i.x == rxp and i.y == rym and rxp <= 7 and rym >= 0 and will[1] == 0:
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rxm and i.y == ryp and ryp <= 7 and rxm >= 0and will[2] == 0:
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxp and i.y == ryp and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                      isit[3] = 1
                                                      will[3] = 1

                                              for i in elementsk:
                                                  if i.x == rxm and i.y == rym and rym >= 0 and rxm >= 0and will[0] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      will[0] = 1
                                                      isit[0] = 1
                                                  if i.x == rxp and i.y == rym and rxp <= 7 and rym >= 0 and will[1] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rxm and i.y == ryp and ryp <= 7 and rxm >= 0 and will[2] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxp and i.y == ryp and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[3] = 1
                                                      will[3] = 1

                                              if isit[0] == 0 and rym >= 0 and rxm >=0 and will[0] == 0:
                                                  temp = simple(rxm, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[rym] - 8))
                                              if isit[1] == 0 and rxp <= 7 and rym >=0 and will[1] == 0:
                                                  temp = simple(rxp, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[rym] - 8))
                                              if isit[2] == 0 and ryp <= 7 and rxm >=0 and will[2] == 0:
                                                  temp = simple(rxm, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[ryp] - 8))
                                              if isit[3] == 0 and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                  temp = simple(rxp, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[ryp] - 8))

                                              pygame.display.update()

                                              
                                      if blah.num == 6:
                                          rx = blah.x
                                          ry = blah.y
                                          rxm = blah.x
                                          ryp = blah.y
                                          rxp = blah.x
                                          rym = blah.y
                                          will = [0,0,0,0]
                                          for i in range(7):
                                              rxm -= 1
                                              rxp += 1
                                              rym -= 1
                                              ryp += 1

                                              isit = [0,0,0,0]
                                              for i in elementss:
                                                  if i.x == rx and i.y == rym and rym >= 0 and will[0] == 0:
                                                      isit[0] = 1
                                                      will[0] = 1
                                                  if i.x == rxp and i.y == ry and rxp <= 7 and will[1] == 0:
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rx and i.y == ryp and ryp <= 7 and will[2] == 0:
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxm and i.y == ry and rxm >= 0 and will[3] == 0:
                                                      isit[3] = 1
                                                      will[3] = 1

                                              for i in elementsk:
                                                  if i.x == rx and i.y == rym and rym >= 0 and will[0] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      will[0] = 1
                                                      isit[0] = 1
                                                  if i.x == rxp and i.y == ry and rxp <= 7 and will[1] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rx and i.y == ryp and ryp <= 7 and will[2] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxm and i.y == ry and rxm >= 0 and will[3] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[3] = 1
                                                      will[3] = 1

                                              if isit[0] == 0 and rym >= 0 and will[0] == 0:
                                                  temp = simple(rx, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[rym] - 8))
                                              if isit[1] == 0 and rxp <= 7 and will[1] == 0:
                                                  temp = simple(rxp, ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[ry] - 8))
                                              if isit[2] == 0 and ryp <= 7 and will[2] == 0:
                                                  temp = simple(rx, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[ryp] - 8))
                                              if isit[3] == 0 and rxm >= 0 and will[3] == 0:
                                                  temp = simple(rxm, ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[ry] - 8))

                                              pygame.display.update()
                                                  
                                                  
                                            
                                      if blah.num == 7:
                                          gx = blah.x
                                          gy = blah.y
                                          isit = [0,0,0,0,0,0,0,0]

                                          for i in elementss:
                                              if i.x == gx - 1 and i.y == gy - 2 and gx > 0 and gy > 1:
                                                  isit[0] = 1
                                              if i.x == gx + 1 and i.y == gy - 2 and gx < 7 and gy > 1:
                                                  isit[1] = 1
                                              if i.x == gx - 2 and i.y == gy - 1 and gx > 1 and gy > 0:
                                                  isit[2] = 1
                                              if i.x == gx + 2 and i.y == gy - 1 and gx < 6 and gy > 0:
                                                  isit[3] = 1
                                              if i.x == gx - 2 and i.y == gy + 1 and gx > 1 and gy < 7:
                                                  isit[4] = 1    
                                              if i.x == gx + 2 and i.y == gy + 1 and gx < 6 and gy < 7:
                                                  isit[5] = 1
                                              if i.x == gx - 1 and i.y == gy + 2 and gx > 0 and gy < 6:
                                                  isit[6] = 1
                                              if i.x == gx + 1 and i.y == gy + 2 and gx < 7 and gy < 6:
                                                  isit[7] = 1

                                          for i in elementsk:
                                              if i.x == gx - 1 and i.y == gy - 2 and gx > 0 and gy > 1:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[0] = 1
                                              if i.x == gx + 1 and i.y == gy - 2 and gx < 7 and gy > 1:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[1] = 1
                                              if i.x == gx - 2 and i.y == gy - 1 and gx > 1 and gy > 0:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[2] = 1
                                              if i.x == gx + 2 and i.y == gy - 1 and gx < 6 and gy > 0:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[3] = 1
                                              if i.x == gx - 2 and i.y == gy + 1 and gx > 1 and gy < 7:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[4] = 1    
                                              if i.x == gx + 2 and i.y == gy + 1 and gx < 6 and gy < 7:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[5] = 1
                                              if i.x == gx - 1 and i.y == gy + 2 and gx > 0 and gy < 6:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[6] = 1
                                              if i.x == gx + 1 and i.y == gy + 2 and gx < 7 and gy < 6:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[7] = 1

                                          if isit[0] == 0 and gx > 0 and gy > 1:
                                                  temp = simple(gx - 1, gy - 2)
                                                  win.blit(blue, (posx[gx - 1] - 7, posy[gy - 2] - 8))
                                                  possible.append(temp)
                                          if isit[1] == 0 and gx < 7 and gy > 1:
                                                  temp = simple(gx + 1, gy - 2)
                                                  win.blit(blue, (posx[gx + 1] - 7, posy[gy - 2] - 8))
                                                  possible.append(temp)
                                          if isit[2] == 0 and gx > 1 and gy > 0:
                                                  temp = simple(gx - 2, gy - 1)
                                                  win.blit(blue, (posx[gx - 2] - 7, posy[gy - 1] - 8))
                                                  possible.append(temp)
                                          if isit[3] == 0 and gx < 6 and gy > 0:
                                                  temp = simple(gx + 2, gy - 1)
                                                  win.blit(blue, (posx[gx + 2] - 7, posy[gy - 1] - 8))
                                                  possible.append(temp)
                                          if isit[4] == 0 and gx > 1 and gy < 7:
                                                  temp = simple(gx - 2, gy + 1)
                                                  win.blit(blue, (posx[gx - 2] - 7, posy[gy + 1] - 8))
                                                  possible.append(temp)
                                          if isit[5] == 0 and gx < 6 and gy < 7:
                                                  temp = simple(gx + 2, gy + 1)
                                                  win.blit(blue, (posx[gx + 2] - 7, posy[gy + 1] - 8))
                                                  possible.append(temp)
                                          if isit[6] == 0 and gx > 0 and gy < 6:
                                                  temp = simple(gx - 1, gy + 2)
                                                  win.blit(blue, (posx[gx - 1] - 7, posy[gy + 2] - 8))
                                                  possible.append(temp)
                                          if isit[7] == 0 and gx < 7 and gy < 6:
                                                  temp = simple(gx + 1, gy + 2)
                                                  win.blit(blue, (posx[gx + 1] - 7, posy[gy + 2] - 8))
                                                  possible.append(temp)

                                      pygame.display.update()
                                              
                                      
                                      if blah.num == 10:
                                          rx = blah.x
                                          ry = blah.y
                                          isit = [0,0,0,0,0,0,0,0]
                                          
                                          for i in elementss:
                                              if i.x == rx - 1 and i.y == ry - 1 and rx > 0 and ry > 0:
                                                  isit[0] = 1
                                              if i.x == rx - 1 and i.y == ry and rx > 0:
                                                  isit[1] = 1
                                              if i.x == rx - 1 and i.y == ry + 1 and rx > 0 and ry < 7:
                                                  isit[2] = 1
                                              if i.x == rx and i.y == ry - 1 and ry > 0:
                                                  isit[3] = 1
                                              if i.x == rx and i.y == ry + 1 and ry < 7:
                                                  isit[4] = 1
                                              if i.x == rx + 1 and i.y == ry - 1 and rx < 7 and ry > 0:
                                                  isit[5] = 1
                                              if i.x == rx + 1 and i.y == ry and rx < 7:
                                                  isit[6] = 1
                                              if i.x == rx + 1 and i.y == ry + 1 and rx < 7 and ry < 7:
                                                  isit[7] = 1
                                                  
                                          for i in elementsk:
                                              if i.x == rx - 1 and i.y == ry - 1 and rx > 0 and ry > 0:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[0] = 1
                                              if i.x == rx - 1 and i.y == ry and rx > 0:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[1] = 1
                                              if i.x == rx - 1 and i.y == ry + 1 and rx > 0 and ry < 7:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[2] = 1
                                              if i.x == rx and i.y == ry - 1 and ry > 0:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[3] = 1
                                              if i.x == rx and i.y == ry + 1 and ry < 7:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[4] = 1
                                              if i.x == rx + 1 and i.y == ry - 1 and rx < 7 and ry > 0:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[5] = 1
                                              if i.x == rx + 1 and i.y == ry and rx < 7:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[6] = 1
                                              if i.x == rx + 1 and i.y == ry + 1 and rx < 7 and ry < 7:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[7] = 1
                                              
                                          if isit[0] == 0 and rx > 0 and ry > 0:
                                                  temp = simple(rx - 1,ry - 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx - 1] - 7, posy[ry - 1] - 8))
                                          if isit[1] == 0 and rx > 0:
                                                  temp = simple(rx - 1,ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx - 1] - 7, posy[ry] - 8))
                                          if isit[2] == 0 and rx > 0 and ry < 7:
                                                  temp = simple(rx - 1,ry + 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx - 1] - 7, posy[ry + 1] - 8))
                                          if isit[3] == 0 and ry > 0:
                                                  temp = simple(rx,ry - 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[ry - 1] - 8))
                                          if isit[4] == 0 and ry < 7:
                                                  temp = simple(rx,ry + 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[ry + 1] - 8))
                                          if isit[5] == 0 and rx < 7 and ry > 0:
                                                  temp = simple(rx + 1,ry - 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx + 1] - 7, posy[ry -1] - 8))
                                          if isit[6] == 0 and rx < 7:
                                                  temp = simple(rx + 1,ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx + 1] - 7, posy[ry] - 8))
                                          if isit[7] == 0 and rx < 7 and ry < 7:
                                                  temp = simple(rx + 1,ry + 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx + 1] - 7, posy[ry + 1] - 8))

                                          pygame.display.update()                           
                                          
                                      if blah.num == 11:
                                          for i in elementsk:
                                              if i.y == blah.y - 1:
                                                  if i.x == blah.x -1:
                                                      possible.append(i)
                                                      win.blit(red, (posx[i.x] - 7,posy[i.y] - 8))
                                                      pygame.display.update()
                                                  if i.x == blah.x + 1:
                                                      possible.append(i)
                                                      win.blit(red, (posx[i.x] - 7,posy[i.y] - 8))
                                                      pygame.display.update()                                                 
                                          if blah.y-1 != -1:
                                              isit = 0
                                              for i in elementss:
                                                  if i.x != blah.x or i.y != blah.y - 1:
                                                      isit += 1
                                              for i in elementsk:
                                                  if i.x != blah.x or i.y != blah.y - 1:
                                                      isit += 1
                                              if isit == total:
                                                  temp = simple(blah.x,blah.y - 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[blah.x]-7, posy[blah.y-1] - 8))
                                                  pygame.display.update()

                            
        else:
            wait = True
            while wait:
                for event in pygame.event.get():
                    
                    if event.type == pygame.QUIT:
                        pygame.quit()

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        for i in possible:
                            if posx[i.x] - 2 < mx and posx[i.x] + 60 > mx and posy[i.y] - 1 < my and posy[i.y] + 60 > my:
                                safed = True
                                wait = False
                                for j in elementss:
                                    if j.x == i.x and j.y == i.y:
                                        elementss.remove(j)
                                        total -= 1
                                forthis[0].x = i.x
                                forthis[0].y = i.y
                                continue
                        possible.clear()
                        forthis.clear()
                        draw()
                        
                        if wait:
                            for blah in elementsk:
                                if posx[blah.x] - 2 < mx and posx[blah.x] + 60 > mx and posy[blah.y] - 1 < my and posy[blah.y] + 60 > my:
                                      forthis.append(blah)
                                      win.blit(green, (posx[blah.x]-7, posy[blah.y] - 8))
                                      pygame.display.update()
                                      if blah.num == 4:
                                          rx = blah.x
                                          ry = blah.y
                                          rxm = blah.x
                                          ryp = blah.y
                                          rxp = blah.x
                                          rym = blah.y
                                          will = [0,0,0,0,0,0,0,0]
                                          for i in range(7):
                                              rxm -= 1
                                              rxp += 1
                                              rym -= 1
                                              ryp += 1

                                              isit = [0,0,0,0,0,0,0,0]
                                              for i in elementsk:
                                                  if i.x == rxm and i.y == rym and rym >= 0 and rxm >= 0 and will[0] == 0:
                                                      isit[0] = 1
                                                      will[0] = 1
                                                  if i.x == rxp and i.y == rym and rxp <= 7 and rym >= 0 and will[1] == 0:
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rxm and i.y == ryp and ryp <= 7 and rxm >= 0and will[2] == 0:
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxp and i.y == ryp and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                      isit[3] = 1
                                                      will[3] = 1
                                                  if i.x == rx and i.y == rym and rym >= 0 and will[4] == 0:
                                                      isit[4] = 1
                                                      will[4] = 1
                                                  if i.x == rxp and i.y == ry and rxp <= 7 and will[5] == 0:
                                                      isit[5] = 1
                                                      will[5] = 1
                                                  if i.x == rx and i.y == ryp and ryp <= 7 and will[6] == 0:
                                                      isit[6] = 1
                                                      will[6] = 1
                                                  if i.x == rxm and i.y == ry and rxm >= 0 and will[7] == 0:
                                                      isit[7] = 1
                                                      will[7] = 1

                                              for i in elementss:
                                                  if i.x == rxm and i.y == rym and rym >= 0 and rxm >= 0and will[0] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      will[0] = 1
                                                      isit[0] = 1
                                                  if i.x == rxp and i.y == rym and rxp <= 7 and rym >= 0 and will[1] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rxm and i.y == ryp and ryp <= 7 and rxm >= 0 and will[2] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxp and i.y == ryp and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[3] = 1
                                                      will[3] = 1
                                                  if i.x == rx and i.y == rym and rym >= 0 and will[4] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      will[4] = 1
                                                      isit[4] = 1
                                                  if i.x == rxp and i.y == ry and rxp <= 7 and will[5] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[5] = 1
                                                      will[5] = 1
                                                  if i.x == rx and i.y == ryp and ryp <= 7 and will[6] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[6] = 1
                                                      will[6] = 1
                                                  if i.x == rxm and i.y == ry and rxm >= 0 and will[7] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[7] = 1
                                                      will[7] = 1

                                              if isit[0] == 0 and rym >= 0 and rxm >=0 and will[0] == 0:
                                                  temp = simple(rxm, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[rym] - 8))
                                              if isit[1] == 0 and rxp <= 7 and rym >=0 and will[1] == 0:
                                                  temp = simple(rxp, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[rym] - 8))
                                              if isit[2] == 0 and ryp <= 7 and rxm >=0 and will[2] == 0:
                                                  temp = simple(rxm, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[ryp] - 8))
                                              if isit[3] == 0 and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                  temp = simple(rxp, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[ryp] - 8))
                                              if isit[4] == 0 and rym >= 0 and will[4] == 0:
                                                  temp = simple(rx, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[rym] - 8))
                                              if isit[5] == 0 and rxp <= 7 and will[5] == 0:
                                                  temp = simple(rxp, ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[ry] - 8))
                                              if isit[6] == 0 and ryp <= 7 and will[6] == 0:
                                                  temp = simple(rx, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[ryp] - 8))
                                              if isit[7] == 0 and rxm >= 0 and will[7] == 0:
                                                  temp = simple(rxm, ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[ry] - 8))

                                              pygame.display.update()

                                              
                                      if blah.num == 2:
                                          rxm = blah.x
                                          ryp = blah.y
                                          rxp = blah.x
                                          rym = blah.y
                                          will = [0,0,0,0]
                                          for i in range(7):
                                              rxm -= 1
                                              rxp += 1
                                              rym -= 1
                                              ryp += 1

                                              isit = [0,0,0,0]
                                              for i in elementsk:
                                                  if i.x == rxm and i.y == rym and rym >= 0 and rxm >= 0 and will[0] == 0:
                                                      isit[0] = 1
                                                      will[0] = 1
                                                  if i.x == rxp and i.y == rym and rxp <= 7 and rym >= 0 and will[1] == 0:
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rxm and i.y == ryp and ryp <= 7 and rxm >= 0and will[2] == 0:
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxp and i.y == ryp and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                      isit[3] = 1
                                                      will[3] = 1

                                              for i in elementss:
                                                  if i.x == rxm and i.y == rym and rym >= 0 and rxm >= 0and will[0] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      will[0] = 1
                                                      isit[0] = 1
                                                  if i.x == rxp and i.y == rym and rxp <= 7 and rym >= 0 and will[1] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rxm and i.y == ryp and ryp <= 7 and rxm >= 0 and will[2] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxp and i.y == ryp and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[3] = 1
                                                      will[3] = 1

                                              if isit[0] == 0 and rym >= 0 and rxm >=0 and will[0] == 0:
                                                  temp = simple(rxm, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[rym] - 8))
                                              if isit[1] == 0 and rxp <= 7 and rym >=0 and will[1] == 0:
                                                  temp = simple(rxp, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[rym] - 8))
                                              if isit[2] == 0 and ryp <= 7 and rxm >=0 and will[2] == 0:
                                                  temp = simple(rxm, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[ryp] - 8))
                                              if isit[3] == 0 and rxp <= 7 and ryp <= 7 and will[3] == 0:
                                                  temp = simple(rxp, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[ryp] - 8))

                                              pygame.display.update()

                                              
                                      if blah.num == 0:
                                          rx = blah.x
                                          ry = blah.y
                                          rxm = blah.x
                                          ryp = blah.y
                                          rxp = blah.x
                                          rym = blah.y
                                          will = [0,0,0,0]
                                          for i in range(7):
                                              rxm -= 1
                                              rxp += 1
                                              rym -= 1
                                              ryp += 1

                                              isit = [0,0,0,0]
                                              for i in elementsk:
                                                  if i.x == rx and i.y == rym and rym >= 0 and will[0] == 0:
                                                      isit[0] = 1
                                                      will[0] = 1
                                                  if i.x == rxp and i.y == ry and rxp <= 7 and will[1] == 0:
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rx and i.y == ryp and ryp <= 7 and will[2] == 0:
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxm and i.y == ry and rxm >= 0 and will[3] == 0:
                                                      isit[3] = 1
                                                      will[3] = 1

                                              for i in elementss:
                                                  if i.x == rx and i.y == rym and rym >= 0 and will[0] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      will[0] = 1
                                                      isit[0] = 1
                                                  if i.x == rxp and i.y == ry and rxp <= 7 and will[1] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[1] = 1
                                                      will[1] = 1
                                                  if i.x == rx and i.y == ryp and ryp <= 7 and will[2] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[2] = 1
                                                      will[2] = 1
                                                  if i.x == rxm and i.y == ry and rxm >= 0 and will[3] == 0:
                                                      win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                      possible.append(i)
                                                      isit[3] = 1
                                                      will[3] = 1

                                              if isit[0] == 0 and rym >= 0 and will[0] == 0:
                                                  temp = simple(rx, rym)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[rym] - 8))
                                              if isit[1] == 0 and rxp <= 7 and will[1] == 0:
                                                  temp = simple(rxp, ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxp] - 7, posy[ry] - 8))
                                              if isit[2] == 0 and ryp <= 7 and will[2] == 0:
                                                  temp = simple(rx, ryp)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[ryp] - 8))
                                              if isit[3] == 0 and rxm >= 0 and will[3] == 0:
                                                  temp = simple(rxm, ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rxm] - 7, posy[ry] - 8))

                                              pygame.display.update()
                                                  
                                                  
                                            
                                      if blah.num == 1:
                                          gx = blah.x
                                          gy = blah.y
                                          isit = [0,0,0,0,0,0,0,0]

                                          for i in elementsk:
                                              if i.x == gx - 1 and i.y == gy - 2 and gx > 0 and gy > 1:
                                                  isit[0] = 1
                                              if i.x == gx + 1 and i.y == gy - 2 and gx < 7 and gy > 1:
                                                  isit[1] = 1
                                              if i.x == gx - 2 and i.y == gy - 1 and gx > 1 and gy > 0:
                                                  isit[2] = 1
                                              if i.x == gx + 2 and i.y == gy - 1 and gx < 6 and gy > 0:
                                                  isit[3] = 1
                                              if i.x == gx - 2 and i.y == gy + 1 and gx > 1 and gy < 7:
                                                  isit[4] = 1    
                                              if i.x == gx + 2 and i.y == gy + 1 and gx < 6 and gy < 7:
                                                  isit[5] = 1
                                              if i.x == gx - 1 and i.y == gy + 2 and gx > 0 and gy < 6:
                                                  isit[6] = 1
                                              if i.x == gx + 1 and i.y == gy + 2 and gx < 7 and gy < 6:
                                                  isit[7] = 1

                                          for i in elementss:
                                              if i.x == gx - 1 and i.y == gy - 2 and gx > 0 and gy > 1:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[0] = 1
                                              if i.x == gx + 1 and i.y == gy - 2 and gx < 7 and gy > 1:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[1] = 1
                                              if i.x == gx - 2 and i.y == gy - 1 and gx > 1 and gy > 0:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[2] = 1
                                              if i.x == gx + 2 and i.y == gy - 1 and gx < 6 and gy > 0:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[3] = 1
                                              if i.x == gx - 2 and i.y == gy + 1 and gx > 1 and gy < 7:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[4] = 1    
                                              if i.x == gx + 2 and i.y == gy + 1 and gx < 6 and gy < 7:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[5] = 1
                                              if i.x == gx - 1 and i.y == gy + 2 and gx > 0 and gy < 6:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[6] = 1
                                              if i.x == gx + 1 and i.y == gy + 2 and gx < 7 and gy < 6:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[7] = 1

                                          if isit[0] == 0 and gx > 0 and gy > 1:
                                                  temp = simple(gx - 1, gy - 2)
                                                  win.blit(blue, (posx[gx - 1] - 7, posy[gy - 2] - 8))
                                                  possible.append(temp)
                                          if isit[1] == 0 and gx < 7 and gy > 1:
                                                  temp = simple(gx + 1, gy - 2)
                                                  win.blit(blue, (posx[gx + 1] - 7, posy[gy - 2] - 8))
                                                  possible.append(temp)
                                          if isit[2] == 0 and gx > 1 and gy > 0:
                                                  temp = simple(gx - 2, gy - 1)
                                                  win.blit(blue, (posx[gx - 2] - 7, posy[gy - 1] - 8))
                                                  possible.append(temp)
                                          if isit[3] == 0 and gx < 6 and gy > 0:
                                                  temp = simple(gx + 2, gy - 1)
                                                  win.blit(blue, (posx[gx + 2] - 7, posy[gy - 1] - 8))
                                                  possible.append(temp)
                                          if isit[4] == 0 and gx > 1 and gy < 7:
                                                  temp = simple(gx - 2, gy + 1)
                                                  win.blit(blue, (posx[gx - 2] - 7, posy[gy + 1] - 8))
                                                  possible.append(temp)
                                          if isit[5] == 0 and gx < 6 and gy < 7:
                                                  temp = simple(gx + 2, gy + 1)
                                                  win.blit(blue, (posx[gx + 2] - 7, posy[gy + 1] - 8))
                                                  possible.append(temp)
                                          if isit[6] == 0 and gx > 0 and gy < 6:
                                                  temp = simple(gx - 1, gy + 2)
                                                  win.blit(blue, (posx[gx - 1] - 7, posy[gy + 2] - 8))
                                                  possible.append(temp)
                                          if isit[7] == 0 and gx < 7 and gy < 6:
                                                  temp = simple(gx + 1, gy + 2)
                                                  win.blit(blue, (posx[gx + 1] - 7, posy[gy + 2] - 8))
                                                  possible.append(temp)

                                      pygame.display.update()
                                              
                                      
                                      if blah.num == 3:
                                          rx = blah.x
                                          ry = blah.y
                                          isit = [0,0,0,0,0,0,0,0]
                                          
                                          for i in elementsk:
                                              if i.x == rx - 1 and i.y == ry - 1 and rx > 0 and ry > 0:
                                                  isit[0] = 1
                                              if i.x == rx - 1 and i.y == ry and rx > 0:
                                                  isit[1] = 1
                                              if i.x == rx - 1 and i.y == ry + 1 and rx > 0 and ry < 7:
                                                  isit[2] = 1
                                              if i.x == rx and i.y == ry - 1 and ry > 0:
                                                  isit[3] = 1
                                              if i.x == rx and i.y == ry + 1 and ry < 7:
                                                  isit[4] = 1
                                              if i.x == rx + 1 and i.y == ry - 1 and rx < 7 and ry > 0:
                                                  isit[5] = 1
                                              if i.x == rx + 1 and i.y == ry and rx < 7:
                                                  isit[6] = 1
                                              if i.x == rx + 1 and i.y == ry + 1 and rx < 7 and ry < 7:
                                                  isit[7] = 1
                                                  
                                          for i in elementss:
                                              if i.x == rx - 1 and i.y == ry - 1 and rx > 0 and ry > 0:
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  possible.append(i)
                                                  isit[0] = 1
                                              if i.x == rx - 1 and i.y == ry and rx > 0:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[1] = 1
                                              if i.x == rx - 1 and i.y == ry + 1 and rx > 0 and ry < 7:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[2] = 1
                                              if i.x == rx and i.y == ry - 1 and ry > 0:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[3] = 1
                                              if i.x == rx and i.y == ry + 1 and ry < 7:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[4] = 1
                                              if i.x == rx + 1 and i.y == ry - 1 and rx < 7 and ry > 0:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[5] = 1
                                              if i.x == rx + 1 and i.y == ry and rx < 7:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[6] = 1
                                              if i.x == rx + 1 and i.y == ry + 1 and rx < 7 and ry < 7:
                                                  possible.append(i)
                                                  win.blit(red, (posx[i.x] - 7, posy[i.y] - 8))
                                                  isit[7] = 1
                                              
                                          if isit[0] == 0 and rx > 0 and ry > 0:
                                                  temp = simple(rx - 1,ry - 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx - 1] - 7, posy[ry - 1] - 8))
                                          if isit[1] == 0 and rx > 0:
                                                  temp = simple(rx - 1,ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx - 1] - 7, posy[ry] - 8))
                                          if isit[2] == 0 and rx > 0 and ry < 7:
                                                  temp = simple(rx - 1,ry + 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx - 1] - 7, posy[ry + 1] - 8))
                                          if isit[3] == 0 and ry > 0:
                                                  temp = simple(rx,ry - 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[ry - 1] - 8))
                                          if isit[4] == 0 and ry < 7:
                                                  temp = simple(rx,ry + 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx] - 7, posy[ry + 1] - 8))
                                          if isit[5] == 0 and rx < 7 and ry > 0:
                                                  temp = simple(rx + 1,ry - 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx + 1] - 7, posy[ry -1] - 8))
                                          if isit[6] == 0 and rx < 7:
                                                  temp = simple(rx + 1,ry)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx + 1] - 7, posy[ry] - 8))
                                          if isit[7] == 0 and rx < 7 and ry < 7:
                                                  temp = simple(rx + 1,ry + 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[rx + 1] - 7, posy[ry + 1] - 8))

                                          pygame.display.update()                           
                                          
                                      if blah.num == 5:
                                          for i in elementss:
                                              if i.y == blah.y + 1:
                                                  if i.x == blah.x -1:
                                                      possible.append(i)
                                                      win.blit(red, (posx[i.x] - 7,posy[i.y] - 8))
                                                      pygame.display.update()
                                                  if i.x == blah.x + 1:
                                                      possible.append(i)
                                                      win.blit(red, (posx[i.x] - 7,posy[i.y] - 8))
                                                      pygame.display.update()                                                 
                                          if blah.y + 1 != 8:
                                              isit = 0
                                              for i in elementsk:
                                                  if i.x != blah.x or i.y != blah.y + 1:
                                                      isit += 1
                                              for i in elementss:
                                                  if i.x != blah.x or i.y != blah.y + 1:
                                                      isit += 1
                                                      
                                              if isit == total:
                                                  temp = simple(blah.x,blah.y + 1)
                                                  possible.append(temp)
                                                  win.blit(blue, (posx[blah.x]-7, posy[blah.y + 1] - 8))
                                                  pygame.display.update()

    draw()

    
def instructions():
    win.blit(bk, (0,0))
    win.blit(menu, (250, 150))
    win.blit(play, (255, 230))
    win.blit(exiti, (260, 350))
    pygame.display.update()

    wait = True
    while wait:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                wait = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x , y = pygame.mouse.get_pos()
            if x > 250 and x < 400:
                if y > 230 and  y < 340:
                    wait = False
                    game()

                if y > 350 and y < 398:
                    wait = False
                    pygame.quit()

def loop():
    instructions()
    game()

if run:
    loop()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
