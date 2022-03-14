from platform import platform
from colorama import Fore, Back, Style
from os import system

from matplotlib.pyplot import bar
from .characters import barbarian, townHall, wall, king, tile, Hut, colony, bomb, cannon_wall, Fire


# Defining unicode characters
refKing = king()
refcol = colony()
tile = tile()
fire = Fire()
king = king()
th = townHall()
town_hall = townHall()
cannon_wall = cannon_wall()
troop1 = barbarian()
troop2 = barbarian()
troop3 = barbarian()


n = 30  # breadth of village
m = 60  # length of village



# Foundation for village ground
ground = [[tile for col in range(m)] for row in range(n)]


def set_Village():
    for i in range(n):
        for j in range(m):
            # ----------- Huts -------------
            if(i==17 and j==19):
                ground[i][j] = Hut()
            if(i==19 and j==30):
                ground[i][j] = Hut()
            if(i==19 and j==23):
                ground[i][j] = Hut()
            if(i==10 and j==19):
                ground[i][j] = Hut()
            if(i==8 and j==28):
                ground[i][j] = Hut()
            if(i==10 and j==32):
                ground[i][j] = Hut()
            if(i==14 and j==32):
                ground[i][j] = Hut()
            # ------------ Walls ---------------
            if(i==17 and (j==22 or j==23 or j==24 or j==25)):
                ground[i][j] = wall()
            if((i==17 or i==18) and j==25):
                ground[i][j] = wall()
            if(j==22 and (i==16 or i==15 or i==14 or i==12 or i==11 or i==10)):
                ground[i][j] = wall()
            if(i==10 and (j==23 or j==24 or j==25 or j==26 or j==27 or j==28 or j==29)):
                ground[i][j] = wall()
            if(j==29 and (i==13 or i==14 or i==11 or i==12)):
                ground[i][j] = wall()
            if(i==17 and (j==28 or j==29)):
                ground[i][j] = wall()
            if (j==26 and (i==9 or i==8 or i==7)):
                ground[i][j] = wall()
            if (i==12 and (j==30 or j==31 or j==32)):
                ground[i][j] = wall()
            if (i==15 and (j==21 or j==20 or j==19 or j==18)):
                ground[i][j] = wall()
            # ----------- Town hall ------------
            if((i==12 or i==13 or i==14 or i==15) and (j==25 or j==26 or j==27)):
                ground[i][j] = town_hall
            # ----------- Colony ---------------
            if(i==8 and j==24):
                ground[i][j] = colony()
            # --------- Death Trap -------------
            if(i==17 and j==26):
                ground[i][j] = Fire()
            # ----------- Cannon 1 -------------
            if(i==21 and j==14):
                ground[i][j] = bomb()
            if(j==12 and (i==20 or i==21 or i==22)):
                ground[i][j] = cannon_wall
            if(j==16 and (i==20 or i==21 or i==22)):
                ground[i][j] = cannon_wall
            if((i==22 or i==23) and (j==13 or j==14 or j==15)):
                ground[i][j] = cannon_wall
            # ------------ Cannon 2 -------------
            if(i==5 and j==41):
                ground[i][j] = bomb()
            if(j==39 and (i==4 or i==5 or i==6)):
                ground[i][j] = cannon_wall
            if(j==43 and (i==4 or i==5 or i==6)):
                ground[i][j] = cannon_wall
            if(i==6 and (j==40 or j==41 or j==42)):
                ground[i][j] = cannon_wall
            if(i==7 and (j==40 or j==41 or j==42)):
                ground[i][j] = cannon_wall
            # ----------- King ------------------
            if (i==10 and j==14):
                ground[i][j] = king
            # # ----------- Troop 1 ---------------
            # if (i==7 and j==34):
            #     ground[i][j] = troop1
            # # ----------- Troop 2 ---------------
            # if (i==21 and j==33):
            #     ground[i][j] = troop2
            # # ----------- Troop 3 ---------------
            # if (i==7 and j==20):
            #     ground[i][j] = troop3
            
            

def display_Viallge():
    system('clear')
    print()
    print()
    for i in range(n):
        for j in range(m):
            print(ground[i][j].tile, end="")
        print("\n", end="")
    print("Town Hall: ", town_hall._health, end="")
    print("  King: ", king._health, end="")
    print("  Troop 1: ", troop1._health, end="")
    print("  Troop 2: ", troop2._health, end="")
    print("  Troop3: ", troop3._health, end="")
    print()