import pygame
import time
import numpy as np
import threading
pygame.font.init()
ekran = pygame.display.set_mode((843, 843))
pygame.display.set_caption("SUDOKU ÇÖZÜCÜ")

grafik=0
kutu = 40
sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0,
           0, 0, 0, 0, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0,
           0, 0, 0, 0, -1, -1, -1, -1, -1, -1],
          [-1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 0,
           0, 0, 0, 0, -1, -1, -1, -1, -1, -1],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
f = open("thread_adimlari.txt", "w")

dosya = open("oyuntahtasi.txt", "r")
a = 0
b = 0
sat = 0
sut = 0
c1 = 1

# txt deki sayıları 21x21 matrise atan döngü
while 1:

    char1 = dosya.read(1)

    if sat < 6:
        if ord(char1) == 10:
            sat = sat+1
            sut = 0
            b = 0
            a = a+1
            continue
        if char1 == "*":
            sudoku[a][b] = 0

        else:
            sudoku[a][b] = ord(char1)-48
        sut = sut+1
        b = b+1

        if sut == 9:
            sut = 12
            b = 12

    if sat > 5 and sat < 9:

        if ord(char1) == 10:
            sat = sat+1
            sut = 0
            b = 0
            a = a+1
            if sat == 9:
                sut = 6
                b = 6
            continue
        if char1 == "*":
            sudoku[a][b] = 0
        else:
            sudoku[a][b] = ord(char1)-48
        sut = sut+1
        b = b+1

    if sat > 8 and sat < 12:

        if ord(char1) == 10:
            sat = sat+1
            sut = 6
            b = 6
            a = a+1
            if sat == 12:
                sut = 0
                b = 0
            continue
        if char1 == "*":
            sudoku[a][b] = 0
        else:
            sudoku[a][b] = ord(char1)-48
        sut = sut+1
        b = b+1

    if sat > 11 and sat < 15:

        if ord(char1) == 10:
            sat = sat+1
            sut = 0
            b = 0
            a = a+1
            continue
        if char1 == "*":
            sudoku[a][b] = 0
        else:
            sudoku[a][b] = ord(char1)-48
        sut = sut+1
        b = b+1

    if sat > 14:

        if ord(char1) == 10:
            sat = sat+1
            sut = 0
            b = 0
            a = a+1
            if sat == 21:
                break
            continue
        if char1 == "*":
            sudoku[a][b] = 0
        else:
            sudoku[a][b] = ord(char1)-48
        sut = sut+1
        b = b+1
        if sut == 9:
            sut = 12
            b = 12

dosya.close()

font1 = pygame.font.SysFont("Arial", 25)

bas = 0
bit = 0
kayx = 0
kayy = 0
k = 0
y = 0
s = 0


def cizgiler(bas, bit, kayx, kayy):
    # Sudoku çizgileri
    for i in range(10):
        if i % 3 == 0:
            kalinlik = 3
            k = 0
            y = 123
            s = 197
        else:
            kalinlik = 1
            k = 100
            y = 100
            s = 100
            # yatay
        pygame.draw.line(ekran, (k, y, s), (bas, (i * kutu)+kayx),
                         (bas+360, (i * kutu)+kayx), kalinlik)
        # dikey
        pygame.draw.line(ekran, (k, y, s), (((i * kutu)+kayy), bit),
                         (((i * kutu)+kayy), bit+360), kalinlik)


def sayilar():

    for i in range(21):
        for j in range(21):
            if sudoku[i][j] != 0 and sudoku[i][j] != -1:
                # Arka renkler
                pygame.draw.rect(ekran, (200, 200, 200),
                                 (j * kutu, i * kutu, kutu + 1, kutu + 1))
                # Bilinen sayılar
                text1 = font1.render(str(sudoku[i][j]), 1, (0, 0, 0))
                ekran.blit(text1, (j * kutu + 15, i * kutu + 5))


ekran.fill((255, 255, 255))
sayilar()
cizgiler(0, 0, 0, 0)
cizgiler(0, 480, 480, 0)
cizgiler(240, 240, 240, 240)
cizgiler(480, 480, 480, 480)
cizgiler(480, 0, 0, 480)

pygame.display.update()
pygame.time.delay(1000)


def coz(sudoku, sat1, sat2, sut1, sut2, t_adi, hep):

    bos = bos_mu(sudoku, sat1, sat2, sut1, sut2, hep)

    if not bos:
        return True
    else:
        satir, sutun = bos

    for i in range(1, 10):

        if gecerli_mi(sudoku, i, (satir, sutun), sat1, sat2, sut1, sut2, t_adi, hep):
            sudoku[satir][sutun] = i
            f.write(t_adi+'-'+(str)(satir)+'x'+(str)(sutun)+'='+(str)(i)+'\n')
        
            if coz(sudoku, sat1, sat2, sut1, sut2, t_adi, hep):
                return True
            sudoku[satir][sutun] = 0
            f.write(t_adi+'-'+(str)(satir)+'x'+(str)(sutun)+'='+'0'+'\n')
            
            
    return False


def gecerli_mi(sudoku, sayi, konum, sat1, sat2, sut1, sut2, t_adi, hep):

    for i in range(sut1, sut2, hep):
        if sayi == sudoku[konum[0]][i]:

            return False

    for i in range(sat1, sat2, hep):
        if sayi == sudoku[i][konum[1]]:
            return False

    satir = konum[0] // 3
    sutun = konum[1] // 3

    for i in range(satir * 3, (satir * 3) + 3):
        for j in range(sutun * 3, (sutun * 3) + 3):
            if sayi == sudoku[i][j]:
                return False

    if kesisen(sudoku, sayi, konum, hep) == False:
        return False

    return True


def bos_mu(sudoku, sat1, sat2, sut1, sut2, hep):
    for satir in range(sat1, sat2, hep):
        for sutun in range(sut1, sut2, hep):
            if sudoku[satir][sutun] == 0:
                return (satir, sutun)
    return None


def kesisen(sudoku, sayi, konum, hep):

    if konum[0] > 5 and konum[0] < 9 and konum[1] > 5 and konum[1] < 9:

        for i in range(0, 15, hep):
            if sayi == sudoku[konum[0]][i]:
                return False
        for i in range(0, 15, hep):
            if sayi == sudoku[i][konum[1]]:
                return False

    if konum[0] > 5 and konum[0] < 9 and konum[1] > 11 and konum[1] < 15:

        for i in range(6, 21, hep):
            if sayi == sudoku[konum[0]][i]:
                return False
        for i in range(0, 15, hep):
            if sayi == sudoku[i][konum[1]]:
                return False

    if konum[0] > 11 and konum[0] < 15 and konum[1] > 5 and konum[1] < 9:

        for i in range(0, 15, hep):
            if sayi == sudoku[konum[0]][i]:
                return False
        for i in range(6, 21, hep):
            if sayi == sudoku[i][konum[1]]:
                return False

    if konum[0] > 11 and konum[0] < 15 and konum[1] > 11 and konum[1] < 15:

        for i in range(6, 21, hep):
            if sayi == sudoku[konum[0]][i]:
                return False
        for i in range(6, 21, hep):
            if sayi == sudoku[i][konum[1]]:
                return False


arti = 1
eksi = -1
t1 = threading.Thread(target=coz, args=(sudoku, 0, 9, 0, 9, "t1", arti))
t2 = threading.Thread(target=coz, args=(sudoku, 0, 9, 12, 21, "t2", arti))
t3 = threading.Thread(target=coz, args=(sudoku, 12, 21, 0, 9, "t3", arti))
t4 = threading.Thread(target=coz, args=(sudoku, 12, 21, 12, 21, "t4", arti))
t5 = threading.Thread(target=coz, args=(sudoku, 6, 15, 6, 15, "t5", arti))
t6 = threading.Thread(target=coz, args=(sudoku, 8, -1, 8, -1, "t6", eksi))
t7 = threading.Thread(target=coz, args=(sudoku, 8, -1, 20, 11, "t7", eksi))
t8 = threading.Thread(target=coz, args=(sudoku, 20, 11, 8, -1, "t8", eksi))
t9 = threading.Thread(target=coz, args=(sudoku, 20, 11, 20, 11, "t9", eksi))
t10 = threading.Thread(target=coz, args=(sudoku, 14, 5, 14, 5, "t10", eksi))

def besli_thread():
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

def onlu_thread():
    t1.start()
    t6.start()
    t2.start()
    t7.start()
    t3.start()
    t8.start()
    t4.start()
    t9.start()
    t5.start()
    t10.start()

    t1.join()
    t6.join()
    t2.join()
    t7.join()
    t3.join()
    t8.join()
    t4.join()
    t9.join()
    t5.join()
    t10.join()
    
t_sayisi=  5
if t_sayisi == 5:
    besli_thread()
if t_sayisi ==10:
    onlu_thread()      
      

def don():
    for i in range(0, 21):
        for j in range(0, 21):
            if sudoku[i][j] == 0:
                c1 = 0
                return c1


while 1:
    c1 = 1
    c1 = don()
    if c1 == 0:
        print('cozemedim tekrar deniyorum')
        
        t1 = threading.Thread(target=coz, args=(
            sudoku, 0, 9, 0, 9, "t1", arti))
        t2 = threading.Thread(target=coz, args=(
            sudoku, 0, 9, 12, 21, "t2", arti))
        t3 = threading.Thread(target=coz, args=(
            sudoku, 12, 21, 0, 9, "t3", arti))
        t4 = threading.Thread(target=coz, args=(
            sudoku, 12, 21, 12, 21, "t4", arti))
        t5 = threading.Thread(target=coz, args=(
            sudoku, 6, 15, 6, 15, "t5", arti))

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()
        t5.join()
        print(np.matrix(sudoku))
        break

    else:
        break

print(np.matrix(sudoku))

sayilar()
cizgiler(0, 0, 0, 0)
cizgiler(0, 480, 480, 0)
cizgiler(240, 240, 240, 240)
cizgiler(480, 480, 480, 480)
cizgiler(480, 0, 0, 480)
f.close()

pygame.display.update()
pygame.time.delay(5000)


pygame.quit()
