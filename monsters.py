'''
    monsters.py
    
'''


from const import *
from colors import COLORS
import rogue as rog
import math
import dice
import ai
import thing





diplomacy={
    #Factions:
    #(Rogue,Citizens,Deprived,Elite,Watch,Abominations,)
    FACT_ROGUE      : (1,1,1,0,0,0,),
    FACT_CITIZENS   : (1,1,0,0,0,0,),
    FACT_DEPRIVED   : (1,0,1,0,0,0,),
    FACT_ELITE      : (0,1,0,1,1,0,),
    FACT_WATCH      : (0,1,0,1,1,0,),
    FACT_MONSTERS   : (0,0,0,0,0,1,),
}




bestiary={
    # Column names in more detail:
    # Lo qi, Hi qi, Attack, Damage, Dodge, Armor, Speed, Move Speed, Attack Speed, Carrying Capacity, Mass, Gold.
    
#Type,  Name,                   (Lo\ Hi\ At\Dm\DV\AV\Spd\Msp\Asp\FIR\BIO\SIGT\HEAR\CARRY\KG\$$\),   FLAGS,

'@' : ('human',                 (20, 20, 5, 2, 2, 0, 100,100,100, 10, 10, 20, 100, 60,  65, 500, ),(CANEAT,),),
'a' : ('abomination',           (16, 8,  0, 4, -8,2, 100,90, 110, 40, 50, 6,  0,   30,  80, 0,  ),(),),
'b' : ('bug-eyed business guy', (20, 30, 5, 2, 2, 0, 150,120,100, 10, 10, 25, 100, 90,  60, 500, ),(CANEAT,),),
'B' : ('butcher',               (50, 20, 5, 6, -4,0, 100,100,100,  0, 25, 10, 100, 90,  130,300, ),(CANEAT,),),
'L' : ('raving lunatic',        (12, 25, 3, 2, 2, 0, 100,100,100,  0, 15, 10, 0,   60,  50, 0, ),(),), #BABBLES,
'r' : ('ravaged',               (4,  1,  1, 2, -8,-1,100,80, 70,   0,  0, 10, 0,   15,  35, 0,  ),(RAVAGED,),),
'R' : ('orctepus',              (15, 5,  6, 2,-12,0, 100,80, 145,  0, 60, 8,  0,   120, 100,0,  ),(CANEAT,),),
's' : ('slithera',              (6,  15, 10,4, -4,0, 100,33, 150,  0, 20, 5,  0,   35,  30, 0, ),(CANEAT,),),
'U' : ('obese scrupula',        (20, 2,  4, 8,-16,3, 100,50, 90,   0, 55, 10, 0,   85,  140,100,  ),(),),
'V' : ('ash vampire',           (50, 80, 8, 5, 8, 0, 100,120,100, 10, 75, 5,  200, 60,  30, 1000,  ),(MEAN,NVISION,),),
'w' : ('dire wolf',             (12, 3,  12,5, 8, 0, 100,225,115, 15, 15, 15, 0,   20,  50, 0,  ),(RAVAGED,),),
'W' : ('whipmaster',            (24, 10, 5, 5, 4, 2, 100,80, 100, 25, 60, 15, 0,   75,  75, 1000, ),(MEAN,NVISION,),),
'z' : ('zombie',                (8,  1,  0, 3,-12,-1,50, 40, 100,  5, 25, 5,  0,   30,  45, 0,  ),(MEAN,),),


}

corpse_recurrence_percent={
    '@' : 100,
    'a' : 30,
    "A" : 100,
    'b' : 100,
    'B' : 100,
    "C" : 100,
    "d" : 100,
    "E" : 100,
    "I" : 100,
    "j" : 100,
    "O" : 100,
    "p" : 100,
    "P" : 100,
    'r' : 20,
    'R' : 75,
    'S' : 100,
    "t" : 100,
    "T" : 100,
    "u" : 100,
    'U' : 100,
    'V' : 100,
    'W' : 50,
    'z' : 20,
}

    # - item drops are the kinds of things that would usually always be on the corpse,
    # such as body part items. Equips and other carried items are added when the
    # monster is created.

    

# Flag for being ravaged, i.e. needing food or begging severely



#
# Monsters
#

#
# Create monster based on current dungeon level
# plugging in values from the table of monsters (bestiary)
# this monster has no special attributes; has generic name
#
def create_monster(typ,x,y,col,mutate=3):
    
    # get generic monster attributes #
    
    monData = bestiary[typ]
    
    name    = monData[0]
    monst=thing.create_creature(name, typ, x,y, col)
    monst.job = name
    i =1; j = 0;
    monst.stats.hpmax       = monData[i][j]; j+=1
    monst.stats.mpmax       = monData[i][j]; j+=1
    monst.stats.atk         = monData[i][j]; j+=1
    monst.stats.dmg         = monData[i][j]; j+=1
    monst.stats.dfn         = monData[i][j]; j+=1
    monst.stats.arm         = monData[i][j]; j+=1
    monst.stats.spd         = monData[i][j]; j+=1
    monst.stats.msp         = monData[i][j]; j+=1
    monst.stats.asp         = monData[i][j]; j+=1
    monst.stats.resfire     = monData[i][j]; j+=1
    monst.stats.resbio      = monData[i][j]; j+=1
    monst.stats.sight       = monData[i][j]; j+=1
    monst.stats.hearing     = monData[i][j]; j+=1
    monst.stats.carry       = monData[i][j]; j+=1
    monst.mass              = monData[i][j]; j+=1
    monst.purse             = monData[i][j]; j+=1
    i+=1
    for flag in monData[i]:     rog.make(monst,flag) #flags
    #i+=1
    #for item in monData[i]:     rog.give(monst,item) #items
    

    # possibly randomly alter some attributes #
    times = 0
    maxgainz = mutate
    chance = 2
    while (dice.roll(10) <= chance and times < maxgainz ):
        times+=1
        r = dice.roll(6)
        if   r == 1: rog.gain(monst,'atk')
        elif r == 2: rog.gain(monst,'dmg')
        elif r == 3: rog.gain(monst,'arm')
        elif r == 4: rog.gain(monst,'dfn')
        elif r == 5: rog.gain(monst,'hpmax')
    times = 0
    maxdrains = mutate
    chance = 2
    while (dice.roll(10) <= chance and times < maxdrains ):
        times+=1
        r = dice.roll(6)
        if   r == 1: rog.drain(monst,'atk')
        elif r == 2: rog.drain(monst,'dmg')
        elif r == 3: rog.drain(monst,'arm')
        elif r == 4: rog.drain(monst,'dfn')
        elif r == 5: rog.drain(monst,'hpmax')
    
    #
    
    
    #

    # ai
    #TEMPORARY
    monst.ai = ai.stateless
    
    return monst
    
# end def












'''# level up #
    levels = 1
    for i in range(levels): rog.level(monst)
    '''

