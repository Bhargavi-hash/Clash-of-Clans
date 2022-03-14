from colorama import Back, Fore, Style
import src.playGround as pg
from src.KBin import KBHit
import time

# (10, 14)  -- Initial King Position
# (7, 34)   -- Initial Troop1 position
# (21, 33)  -- Initial Troop2 position
# (7, 20)   -- Initial Troop3 position
# (21, 14)  -- Cannon 1 position
# (5, 41)   -- Cannon 2 Position

c1Row = 21
c1Col = 14

c2Row = 5
c2Col = 41

king_row = 10
king_col = 14

t1_row = 7
t1_col = 34
t1_destRow = 0
t1_destCol = 0


t2_row = 21
t2_col = 34
t2_destRow = 0
t2_destCol = 0


t3_row = 7
t3_col = 20
t3_destRow = 0
t3_destCol = 0


pg.set_Village()
pg.display_Viallge()

'''
--> King Motion Keys

    W - Up
    A - Left
    S - Down
    D - Right
'''

'''
--> Troops Spawn Keys

    J - Top Left
    K - Top Right
    M - Bottom
'''

troop1_onboard = 0
troop2_onboard = 0
troop3_onboard = 0

'''
--> Spell Keys
    
    H - Heal Spell
    R - Rage Spell
'''
MotionKeys = ('A', 'S', 'W', 'D')
SpawnKeys = ('J', 'K', 'M')
SpellKeys = ('H', 'R')


def spawnHelpers(key):
    if key.upper() == 'J':
        return key, t3_row, t3_col
    if key.upper() == 'K':
        return key, t1_row, t1_col
    if key.upper() == 'M':
        return key, t2_row, t2_col


def posHelpers(key):
    addRow = 0
    addCol = 0
    if key.upper() == 'A':
        addCol = -1
        return addRow, addCol
    if key.upper() == 'S':
        addRow = 1
        return addRow, addCol
    if key.upper() == 'W':
        addRow = -1
        return addRow, addCol
    if key.upper() == 'D':
        addCol = 1
        return addRow, addCol


def troopDest(row, col):
    freeze = 0
    min = 1000
    nRow = 0
    nCol = 0
    for i in range(pg.n):
        for j in range(pg.m):
            if(pg.ground[i][j].tile == pg.Hut().tile or pg.ground[i][j].tile == pg.townHall().tile or pg.ground[i][j].tile == pg.townHall().shieldTile):
                dist = (row - i)**2 + (col - j)**2
                if (dist < min):
                    min = dist
                    nRow = i
                    nCol = j
                    freeze = 1
    return freeze, nRow, nCol

def CannonTarget(row, col):
    TargetFound = 0
    targetRow = 0
    targetCol = 0
    for i in range(pg.n):
        for j in range(pg.m):
            if(pg.ground[i][j].tile == pg.barbarian().tile or pg.ground[i][j].tile == pg.refKing.tile):
                dist = (row - i)**2 + (col - j)**2
                if(dist <= pg.bomb()._damageRange**2):
                    targetRow = i
                    targetCol = j
                    TargetFound = 1
    return TargetFound, targetRow, targetCol

def searchBuildings():
    Found = 0
    for i in range(pg.n):
        for j in range(pg.m):
            if(pg.ground[i][j].tile == pg.Hut().tile or pg.ground[i][j].tile == pg.th.tile or pg.ground[i][j].tile == pg.th.shieldTile or pg.ground[i][j].tile == pg.refcol.tile or pg.ground[i][j].tile == pg.refcol.tile):
                Found = 1
    return Found
    

playkey = KBHit()
while True:
    
    if (pg.king._health == pg.troop2._health == pg.troop3._health == pg.troop1._health == 0):
        print(Fore.RED + "Game Over. You Lost :(" + Style.RESET_ALL)
        break
    
    if(searchBuildings()==0 and (pg.king._health >0 or pg.troop1._health > 0 or pg.troop2._health > 0 or pg.troop3._health>0)):
        print(Fore.GREEN + "Game over. You won :)" + Style.RESET_ALL)
        break

    c1Attack, c1TargetRow, c1TargetCol = CannonTarget(c1Row, c1Col)
    c2Attack, c2TargetRow, c2TargetCol = CannonTarget(c2Row, c2Col)

    if(c1Attack == 1):
        print(c1TargetRow, c1TargetCol)
        pg.ground[c1TargetRow][c1TargetCol]._health -= pg.bomb()._damagePower
        if(pg.ground[c1TargetRow][c1TargetCol]._health <= 0):
            pg.ground[c1TargetRow][c1TargetCol]._health = 0
            if (pg.ground[c1TargetRow][c1TargetCol].tile == pg.troop1.tile):
                troop1_onboard = 0
            if (pg.ground[c1TargetRow][c1TargetCol].tile == pg.troop2.tile):
                troop2_onboard = 0
            if (pg.ground[c1TargetRow][c1TargetCol].tile == pg.troop3.tile):
                troop3_onboard = 0
            pg.ground[c1TargetRow][c1TargetCol].tile = pg.tile.tile
        time.sleep(0.5)
        pg.display_Viallge()


    if(c2Attack == 2):
        pg.ground[c2TargetRow][c2TargetCol]._health -= pg.bomb()._damagePower
        if(pg.ground[c2TargetRow][c2TargetCol]._health <= 0):
            pg.ground[c2TargetRow][c2TargetCol]._health = 0
            if (pg.ground[c2TargetRow][c2TargetCol].tile == pg.troop1.tile):
                troop1_onboard = 0
            if (pg.ground[c2TargetRow][c2TargetCol].tile == pg.troop2.tile):
                troop2_onboard = 0
            if (pg.ground[c2TargetRow][c2TargetCol].tile == pg.troop3.tile):
                troop3_onboard = 0
            pg.ground[c2TargetRow][c2TargetCol].tile = pg.tile.tile
        time.sleep(0.5)
        pg.display_Viallge()

    if (playkey.kbhit()):
        key = playkey.getch()

        '''
        # ==================== Implementing Play keys for king's movement =====================
        '''

        if key.upper() in MotionKeys:
            moveRow, moveCol = posHelpers(key)
            if(pg.ground[king_row + moveRow][king_col + moveCol].tile == pg.tile.tile):
                pg.ground[king_row + moveRow][king_col +
                                              moveCol] = pg.ground[king_row][king_col]
                pg.ground[king_row][king_col] = pg.tile
                king_col = king_col + moveCol
                king_row = king_row + moveRow

            '''
                King stepping into fire (Death trap)
            '''

            if(pg.ground[king_row + moveRow][king_col + moveCol].tile == pg.fire.tile):
                pg.ground[king_row][king_col]._health = 0
                pg.ground[king_row][king_col].tile = pg.tile.tile
        '''
        # ====================== Heal Spell ===================================
        '''
        if key.upper() == 'H':
            if(pg.king._health > 0):
                pg.king._health = pg.king._health + 1.5*pg.king._health
            if(troop3_onboard == 1):
                pg.troop3._health = pg.troop3._health + 1.5*pg.troop3._health
            if(troop2_onboard == 1):
                pg.troop2._health = pg.troop2._health + 1.5*pg.troop2._health
            if(troop1_onboard == 1):
                pg.troop1._health = pg.troop1._health + 1.5*pg.troop1._health

        '''
        # ====================== Rage spell =====================================
        '''
        if key.upper() == 'R':
            if(pg.king._health > 0):
                pg.king._damagePower = pg.king._damagePower*2
            if(troop1_onboard == 1):
                pg.troop1._damagePower = pg.troop1._damagePower*2
            if(troop2_onboard == 1):
                pg.troop2._damagePower = pg.troop2._damagePower*2
            if(troop3_onboard == 1):
                pg.troop3._damagePower = pg.troop3._damagePower*2

        '''
        # ======================== king's Axe ==============================
        '''
        if key.upper() == 'X':
            if(pg.king._health > 0):
                for i in range(pg.n):
                    for j in range(pg.m):
                        if (pg.ground[i][j].tile == pg.Hut().tile or pg.ground[i][j].tile == pg.colony().tile):
                            distance = (king_row - i)**2 + (king_col - j)**2
                            if(distance <= pg.king._axeAOE**2):
                                pg.ground[i][j]._health -= pg.king._damagePower
                                if(pg.ground[i][j]._health <= 0):
                                    pg.ground[i][j]._health = 0
                                    pg.ground[i][j].tile = pg.tile.tile
                        if (pg.ground[i][j].tile == pg.town_hall.tile or pg.ground[i][j].tile == pg.town_hall.shieldTile):
                            distance = (king_row - i)**2 + (king_col - j)**2
                            if(distance <= pg.king._axeAOE**2):
                                if (pg.town_hall._shield != 0):
                                    pg.town_hall.tile = pg.town_hall.shieldTile
                                    pg.town_hall._shield -= 1
                                else:
                                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                                    pg.town_hall._health -= pg.king._damagePower
                                    if(pg.town_hall._health <= 0):
                                        pg.town_hall._health = 0
                                        pg.town_hall.tile = pg.tile.tile
        '''
        # ======================== Implementing Attack key for King ===============================
        '''

        if key == " ":
            # ------------------------------------------------------------------------------
            # -------------------- Attacking Huts and Colonies -----------------------------
            # ------------------------------------------------------------------------------

            if(pg.ground[king_row + moveRow][king_col + moveCol].tile == pg.Hut().tile):
                pg.ground[king_row + moveRow][king_col +
                                              moveCol]._health -= pg.ground[king_row][king_col]._damagePower
                if(pg.ground[king_row + moveRow][king_col + moveCol]._health <= 0):
                    pg.ground[king_row + moveRow][king_col +
                                                  moveCol]._health = 0
                    pg.ground[king_row + moveRow][king_col + moveCol] = pg.tile
            if(pg.ground[king_row + moveRow][king_col + moveCol].tile == pg.colony().tile or pg.ground[king_row + moveRow][king_col + moveCol].tile == pg.colony().shieldTile):
                if(pg.ground[king_row + moveRow][king_col + moveCol]._shield != 0):
                    pg.ground[king_row + moveRow][king_col +
                                                  moveCol].tile = pg.ground[king_row + moveRow][king_col + moveCol].shieldTile
                    pg.ground[king_row + moveRow][king_col +
                                                  moveCol]._shield -= 1
                else:
                    pg.ground[king_row + moveRow][king_col +
                                                  moveCol].tile = Back.GREEN + "🏘️" + " " + Style.RESET_ALL
                    pg.ground[king_row + moveRow][king_col +
                                                  moveCol]._health -= pg.ground[king_row][king_col]._damagePower
                    if(pg.ground[king_row + moveRow][king_col + moveCol]._health <= 0):
                        pg.ground[king_row + moveRow][king_col +
                                                      moveCol]._health = 0
                        pg.ground[king_row +
                                  moveRow][king_col + moveCol] = pg.tile

            # ------------------------------------------------------------------------------
            # -------------------- Attacking Village Walls ---------------------------------
            # ------------------------------------------------------------------------------

            if(pg.ground[king_row + moveRow][king_col + moveCol].tile == pg.wall().tile):
                pg.ground[king_row + moveRow][king_col +
                                              moveCol]._health -= pg.ground[king_row][king_col]._damagePower
                if(pg.ground[king_row + moveRow][king_col + moveCol]._health <= 0):
                    pg.ground[king_row + moveRow][king_col +
                                                  moveCol]._health = 0
                    pg.ground[king_row + moveRow][king_col + moveCol] = pg.tile

            '''
                ATTACKING TOWN HALL
            '''
            if(pg.ground[king_row + moveRow][king_col + moveCol].tile == pg.town_hall.tile or pg.ground[king_row + moveRow][king_col + moveCol].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[king_row][king_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
        pg.display_Viallge()
        '''
        # =========================== Spawning Troops ======================================
        '''
        if key.upper() in SpawnKeys:
            tKey, tRow, tCol = spawnHelpers(key)
            if tKey.upper() == 'J':
                pg.ground[tRow][tCol] = pg.troop3
                troop3_onboard = 1
            if tKey.upper() == 'K':
                pg.ground[tRow][tCol] = pg.troop1
                troop1_onboard = 1
            if tKey.upper() == 'M':
                pg.ground[tRow][tCol] = pg.troop2
                troop2_onboard = 1

    '''
    # ========================== Destination of Troops ========================================
    '''
    if (troop1_onboard == 1):
        troop1_onboard, t1_destRow, t1_destCol = troopDest(t1_row, t1_col)
    if (troop2_onboard == 1):
        troop2_onboard, t2_destRow, t2_destCol = troopDest(t2_row, t2_col)
    if (troop3_onboard == 1):
        troop3_onboard, t3_destRow, t3_destCol = troopDest(t3_row, t3_col)

    '''
    # ========================== Troops movement ===============================================
    '''
    if (troop1_onboard == 1):
        if(t1_destRow < t1_row):
            if(pg.ground[t1_row-1][t1_col].tile == pg.tile.tile):
                pg.ground[t1_row-1][t1_col] = pg.ground[t1_row][t1_col]
                pg.ground[t1_row][t1_col] = pg.tile
                t1_row = t1_row - 1
            if(pg.ground[t1_row-1][t1_col].tile == pg.Hut().tile or pg.ground[t1_row-1][t1_col].tile == pg.wall().tile):
                pg.ground[t1_row -
                          1][t1_col]._health -= pg.ground[t1_row][t1_col]._damagePower
                if(pg.ground[t1_row-1][t1_col]._health <= 0):
                    pg.ground[t1_row-1][t1_col]._health = 0
                    pg.ground[t1_row-1][t1_col] = pg.tile
            if(pg.ground[t1_row-1][t1_col].tile == pg.town_hall.tile or pg.ground[t1_row-1][t1_col].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t1_row][t1_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t1_row-1][t1_col] = pg.tile
            if(pg.ground[t1_row-1][t1_col].tile == pg.fire.tile):
                pg.troop1._health = 0
                pg.ground[t1_row][t1_col] = pg.tile
                troop1_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
        if(t1_destRow > t1_row):
            if(pg.ground[t1_row+1][t1_col].tile == pg.tile.tile):
                pg.ground[t1_row+1][t1_col] = pg.ground[t1_row][t1_col]
                pg.ground[t1_row][t1_col] = pg.tile
                t1_row = t1_row + 1
            if(pg.ground[t1_row+1][t1_col].tile == pg.Hut().tile or pg.ground[t1_row+1][t1_col].tile == pg.wall().tile):
                pg.ground[t1_row +
                          1][t1_col]._health -= pg.ground[t1_row][t1_col]._damagePower
                if(pg.ground[t1_row+1][t1_col]._health <= 0):
                    pg.ground[t1_row+1][t1_col]._health = 0
                    pg.ground[t1_row+1][t1_col] = pg.tile
            if(pg.ground[t1_row+1][t1_col].tile == pg.town_hall.tile or pg.ground[t1_row+1][t1_col].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t1_row][t1_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t1_row+1][t1_col] = pg.tile
            if(pg.ground[t1_row+1][t1_col].tile == pg.fire.tile):
                pg.troop1._health = 0
                pg.ground[t1_row][t1_col] = pg.tile
                troop1_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
        if (t1_destCol > t1_col):
            if(pg.ground[t1_row][t1_col+1].tile == pg.tile.tile):
                pg.ground[t1_row][t1_col+1] = pg.ground[t1_row][t1_col]
                pg.ground[t1_row][t1_col] = pg.tile
                t1_col = t1_col + 1
            if(pg.ground[t1_row][t1_col+1].tile == pg.Hut().tile or pg.ground[t1_row][t1_col+1].tile == pg.wall().tile):
                pg.ground[t1_row][t1_col +
                                  1]._health -= pg.ground[t1_row][t1_col]._damagePower
                if(pg.ground[t1_row][t1_col+1]._health <= 0):
                    pg.ground[t1_row][t1_col+1]._health = 0
                    pg.ground[t1_row][t1_col+1] = pg.tile
            if(pg.ground[t1_row][t1_col+1].tile == pg.town_hall.tile or pg.ground[t1_row][t1_col+1].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t1_row][t1_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t1_row][t1_col+1] = pg.tile
            if(pg.ground[t1_row][t1_col+1].tile == pg.fire.tile):
                pg.troop1._health = 0
                pg.ground[t1_row][t1_col] = pg.tile
                troop1_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
        if (t1_destCol < t1_col):
            if(pg.ground[t1_row][t1_col-1].tile == pg.tile.tile):
                pg.ground[t1_row][t1_col-1] = pg.ground[t1_row][t1_col]
                pg.ground[t1_row][t1_col] = pg.tile
                t1_col = t1_col - 1
            if(pg.ground[t1_row][t1_col-1].tile == pg.Hut().tile or pg.ground[t1_row][t1_col-1].tile == pg.wall().tile):
                pg.ground[t1_row][t1_col -
                                  1]._health -= pg.ground[t1_row][t1_col]._damagePower
                if(pg.ground[t1_row][t1_col-1]._health <= 0):
                    pg.ground[t1_row][t1_col-1]._health = 0
                    pg.ground[t1_row][t1_col-1] = pg.tile
            if(pg.ground[t1_row][t1_col-1].tile == pg.town_hall.tile or pg.ground[t1_row][t1_col-1].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t1_row][t1_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t1_row][t1_col-1] = pg.tile
            if(pg.ground[t1_row][t1_col-1].tile == pg.fire.tile):
                pg.troop1._health = 0
                pg.ground[t1_row][t1_col] = pg.tile
                troop1_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
    if (troop2_onboard == 1):
        if(t2_destRow < t2_row):
            if(pg.ground[t2_row-1][t2_col].tile == pg.tile.tile):
                pg.ground[t2_row-1][t2_col] = pg.ground[t2_row][t2_col]
                pg.ground[t2_row][t2_col] = pg.tile
                t2_row = t2_row - 1
            if(pg.ground[t2_row-1][t2_col].tile == pg.Hut().tile or pg.ground[t2_row-1][t2_col].tile == pg.wall().tile):
                pg.ground[t2_row -
                          1][t2_col]._health -= pg.ground[t2_row][t2_col]._damagePower
                if(pg.ground[t2_row-1][t2_col]._health <= 0):
                    pg.ground[t2_row-1][t2_col]._health = 0
                    pg.ground[t2_row-1][t2_col] = pg.tile
            if(pg.ground[t2_row-1][t2_col].tile == pg.town_hall.tile or pg.ground[t2_row-1][t2_col].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t2_row][t2_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t2_row-1][t2_col] = pg.tile
            if(pg.ground[t2_row-1][t2_col].tile == pg.fire.tile):
                pg.troop2._health = 0
                pg.ground[t2_row][t2_col] = pg.tile
            time.sleep(0.2)
            pg.display_Viallge()
        if(t2_destRow > t2_row):
            if(pg.ground[t2_row+1][t2_col].tile == pg.tile.tile):
                pg.ground[t2_row+1][t2_col] = pg.ground[t2_row][t2_col]
                pg.ground[t2_row][t2_col] = pg.tile
                t2_row = t2_row + 1
            if(pg.ground[t2_row+1][t2_col].tile == pg.Hut().tile or pg.ground[t2_row+1][t2_col].tile == pg.wall().tile):
                pg.ground[t2_row +
                          1][t2_col]._health -= pg.ground[t2_row][t2_col]._damagePower
                if(pg.ground[t2_row+1][t2_col]._health <= 0):
                    pg.ground[t2_row+1][t2_col]._health = 0
                    pg.ground[t2_row+1][t2_col] = pg.tile
            if(pg.ground[t2_row+1][t2_col].tile == pg.town_hall.tile or pg.ground[t2_row+1][t2_col].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t2_row][t2_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t2_row+1][t2_col] = pg.tile
            if(pg.ground[t2_row+1][t2_col].tile == pg.fire.tile):
                pg.troop2._health = 0
                pg.ground[t2_row][t2_col] = pg.tile
                troop2_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
        if (t2_destCol > t2_col):
            if(pg.ground[t2_row][t2_col+1].tile == pg.tile.tile):
                pg.ground[t2_row][t2_col+1] = pg.ground[t2_row][t2_col]
                pg.ground[t2_row][t2_col] = pg.tile
                t2_col = t2_col + 1
            if(pg.ground[t2_row][t2_col+1].tile == pg.Hut().tile or pg.ground[t2_row][t2_col+1].tile == pg.wall().tile):
                pg.ground[t2_row][t2_col +
                                  1]._health -= pg.ground[t2_row][t2_col]._damagePower
                if(pg.ground[t2_row][t2_col+1]._health <= 0):
                    pg.ground[t2_row][t2_col+1]._health = 0
                    pg.ground[t2_row][t2_col+1] = pg.tile
            if(pg.ground[t2_row][t2_col+1].tile == pg.town_hall.tile or pg.ground[t2_row][t2_col+1].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t2_row][t2_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t2_row][t2_col+1] = pg.tile
            if(pg.ground[t2_row][t2_col+1].tile == pg.fire.tile):
                pg.troop2._health = 0
                pg.ground[t2_row][t2_col] = pg.tile
                troop2_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
        if (t2_destCol < t2_col):
            if(pg.ground[t2_row][t2_col-1].tile == pg.tile.tile):
                pg.ground[t2_row][t2_col-1] = pg.ground[t2_row][t2_col]
                pg.ground[t2_row][t2_col] = pg.tile
                t2_col = t2_col - 1
            if(pg.ground[t2_row][t2_col-1].tile == pg.Hut().tile or pg.ground[t2_row][t2_col-1].tile == pg.wall().tile):
                pg.ground[t2_row][t2_col -
                                  1]._health -= pg.ground[t2_row][t2_col]._damagePower
                if(pg.ground[t2_row][t2_col-1]._health <= 0):
                    pg.ground[t2_row][t2_col-1]._health = 0
                    pg.ground[t2_row][t2_col-1] = pg.tile
            if(pg.ground[t2_row][t2_col-1].tile == pg.town_hall.tile or pg.ground[t2_row][t2_col-1].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t2_row][t2_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t2_row][t2_col-1] = pg.tile
            if(pg.ground[t2_row][t2_col-1].tile == pg.fire.tile):
                pg.troop2._health = 0
                pg.ground[t2_row][t2_col] = pg.tile
                troop2_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
    if (troop3_onboard == 1):
        if(t3_destRow < t3_row):
            if(pg.ground[t3_row-1][t3_col].tile == pg.tile.tile):
                pg.ground[t3_row-1][t3_col] = pg.ground[t3_row][t3_col]
                pg.ground[t3_row][t3_col] = pg.tile
                t3_row = t3_row - 1
            if(pg.ground[t3_row-1][t3_col].tile == pg.Hut().tile or pg.ground[t3_row-1][t3_col].tile == pg.wall().tile):
                pg.ground[t3_row -
                          1][t3_col]._health -= pg.ground[t3_row][t3_col]._damagePower
                if(pg.ground[t3_row-1][t3_col]._health <= 0):
                    pg.ground[t3_row-1][t3_col]._health = 0
                    pg.ground[t3_row-1][t3_col] = pg.tile
            if(pg.ground[t3_row-1][t3_col].tile == pg.town_hall.tile or pg.ground[t3_row-1][t3_col].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t3_row][t3_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t3_row-1][t3_col] = pg.tile
            if(pg.ground[t3_row-1][t3_col].tile == pg.fire.tile):
                pg.troop3._health = 0
                pg.ground[t3_row][t3_col] = pg.tile
                troop3_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
        if(t3_destRow > t3_row):
            if(pg.ground[t3_row+1][t3_col].tile == pg.tile.tile):
                pg.ground[t3_row+1][t3_col] = pg.ground[t3_row][t3_col]
                pg.ground[t3_row][t3_col] = pg.tile
                t3_row = t3_row + 1
            if(pg.ground[t3_row+1][t3_col].tile == pg.Hut().tile or pg.ground[t3_row+1][t3_col].tile == pg.wall().tile):
                pg.ground[t3_row +
                          1][t3_col]._health -= pg.ground[t3_row][t3_col]._damagePower
                if(pg.ground[t3_row+1][t3_col]._health <= 0):
                    pg.ground[t3_row+1][t3_col]._health = 0
                    pg.ground[t3_row+1][t3_col] = pg.tile
            if(pg.ground[t3_row+1][t3_col].tile == pg.town_hall.tile or pg.ground[t3_row+1][t3_col].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t3_row][t3_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t3_row+1][t3_col] = pg.tile
            if(pg.ground[t3_row+1][t3_col].tile == pg.fire.tile):
                pg.troop3._health = 0
                pg.ground[t3_row][t3_col] = pg.tile
                troop3_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
        if (t3_destCol > t3_col):
            if(pg.ground[t3_row][t3_col+1].tile == pg.tile.tile):
                pg.ground[t3_row][t3_col+1] = pg.ground[t3_row][t3_col]
                pg.ground[t3_row][t3_col] = pg.tile
                t3_col = t3_col + 1
            if(pg.ground[t3_row][t3_col+1].tile == pg.Hut().tile or pg.ground[t3_row][t3_col+1].tile == pg.wall().tile):
                pg.ground[t3_row][t3_col +
                                  1]._health -= pg.ground[t3_row][t3_col]._damagePower
                if(pg.ground[t3_row][t3_col+1]._health <= 0):
                    pg.ground[t3_row][t3_col+1]._health = 0
                    pg.ground[t3_row][t3_col+1] = pg.tile
            if(pg.ground[t3_row][t3_col+1].tile == pg.town_hall.tile or pg.ground[t3_row][t3_col+1].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t3_row][t3_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t3_row][t3_col+1] = pg.tile
            if(pg.ground[t3_row][t3_col+1].tile == pg.fire.tile):
                pg.troop3._health = 0
                pg.ground[t3_row][t3_col] = pg.tile
                troop3_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
        if (t3_destCol < t3_col):
            if(pg.ground[t3_row][t3_col-1].tile == pg.tile.tile):
                pg.ground[t3_row][t3_col-1] = pg.ground[t3_row][t3_col]
                pg.ground[t3_row][t3_col] = pg.tile
                t3_col = t3_col - 1
            if(pg.ground[t3_row][t3_col-1].tile == pg.Hut().tile or pg.ground[t3_row][t3_col-1].tile == pg.wall().tile):
                pg.ground[t3_row][t3_col -
                                  1]._health -= pg.ground[t3_row][t3_col]._damagePower
                if(pg.ground[t3_row][t3_col-1]._health <= 0):
                    pg.ground[t3_row][t3_col-1]._health = 0
                    pg.ground[t3_row][t3_col-1] = pg.tile
            if(pg.ground[t3_row][t3_col-1].tile == pg.town_hall.tile or pg.ground[t3_row][t3_col-1].tile == pg.town_hall.shieldTile):
                if(pg.town_hall._shield != 0):
                    pg.town_hall.tile = pg.town_hall.shieldTile
                    pg.town_hall._shield -= 1
                else:
                    pg.town_hall.tile = Back.GREEN + "🏛️" + " " + Style.RESET_ALL
                    pg.town_hall._health -= pg.ground[t3_row][t3_col]._damagePower
                    if(pg.town_hall._health <= 0):
                        pg.town_hall._health = 0
                        pg.town_hall.shieldTile = pg.tile.tile
                        pg.town_hall.tile = pg.tile.tile
                        pg.ground[t3_row][t3_col-1] = pg.tile
            if(pg.ground[t3_row][t3_col-1].tile == pg.fire.tile):
                pg.troop3._health = 0
                pg.ground[t3_row][t3_col] = pg.tile
                troop3_onboard = 0
            time.sleep(0.2)
            pg.display_Viallge()
