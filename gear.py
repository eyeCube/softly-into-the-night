'''
    gear.py

    Armor, helmets
    Functions for making gear items
'''


import random

from const import *
from colors import COLORS as COL
import rogue as rog
import thing
import action



ARMR = T_ARMOR
HELM = T_HELMET
BACK = T_CLOAK

NUMWPNSTATS = 3

MEL     = T_MELEEWEAPON
THRO    = T_THROWWEAPON
ENER    = T_ENERGYWEAPON
HEVY    = T_HEAVYWEAPON
GUN     = T_GUN

#ARRO    = T_ARROW
#BOW     = T_BOW

FLSH = MAT_FLESH
LETH = MAT_LEATHER
CLTH = MAT_CLOTH
WOOD = MAT_WOOD
BONE = MAT_BONE
CARB = MAT_CARBON
PLAS = MAT_PLASTIC
METL = MAT_METAL

A_ELEC = AMMO_ELEC
A_BULL = AMMO_BULLETS
A_BALL = AMMO_BALLS
A_SHOT = AMMO_SHOT
A_FLUID= AMMO_FLUIDS
A_OIL  = AMMO_OIL
A_HAZM = AMMO_HAZMATS
A_ACID = AMMO_ACID
A_CHEM = AMMO_CHEMS
#A_ARRO = AMMO_ARROWS

PH = ELEM_PHYS
FI = ELEM_FIRE
BI = ELEM_BIO
CH = ELEM_CHEM
EL = ELEM_ELEC
RA = ELEM_RADS


#GEAR
    #Columns:
    #   $$$$$   cost
    #   KG      mass
    #   Dur     durability
    #   Mat     material
    #   DV      Dodge Value
    #   AV      Armor Value
    #   Msp     Move Speed
    #   Vis     Vision
    #   FIR     Fire Resist
    #   BIO     Bio Resist
    #
GEAR = {
#--Name-----------------------Type,Dlv,$$$$$, KG,   Dur, Mat, (DV, AV, MSp, Vis,FIR,BIO,ELE)
    #Back
"cloak"                     :(BACK,1,  420,   6.0,  150, CLTH,( 4,  1, -3,  0,  10, 10, 0,), ),
    #Armor
"skin suit"                 :(ARMR,1,  450,   14.7, 90,  FLSH,( 2,  2, -6,  0,  0,  10, 3,), ),
"boiled leather plate"      :(ARMR,1,  975,   12.5, 180, LETH,( 0,  3, -6,  0,  5,  5,  15,), ),
"bone armor"                :(ARMR,2,  890,   27.8, 475, BONE,(-6,  5, -18, 0,  15, 10, 0,), ),
"carb garb"                 :(ARMR,2,  1100,  22.5, 600, CARB,(-3,  3, -12, 0,  10, 10, 0,), ),
"riot gear"                 :(ARMR,3,  3490,  20.5, 800, CARB,(-2,  6, -12, 0,  33, 25, 0,), ),
"metal gear"                :(ARMR,12, 9950,  27.5, 1000,METL,(-4,  8, -18, 0,  5,  5,  -10,), ),
"full metal suit"           :(ARMR,14, 12000, 35.1, 1200,METL,(-5,  10,-21, 0,  5,  10, -20,), ),
"graphene armor"            :(ARMR,18, 58250, 16.5, 900, CARB,(-2,  12,-9,  0,  20, 20, 25,), ),
"space suit"                :(ARMR,15, 36000, 40.0, 50,  CARB,(-15, 3, -33, 0,  20, 40, 5,), ),
"hazard suit"               :(ARMR,10, 2445,  14.5, 75,  PLAS,(-12, 2, -24, 0,  5,  50, 10,), ),
"disposable PPE"            :(ARMR,1,  110,   9.25, 25,  PLAS,(-9,  1, -15, 0,  -15,30, 5,), ),
"wetsuit"                   :(ARMR,3,  1600,  8.2,  50,  PLAS,( 0,  0, -6,  0,  33, 5,  21,), ),
"fire blanket"              :(BACK,4,  600,   12.4, 175, CLTH,(-3,  1, -9,  0,  40, 15, 10,), ),
"burn jacket"               :(ARMR,8,  1965,  19.5, 150, CLTH,(-5,  2, -12, 0,  55, 15, 15,), ),
    #Helmets
"bandana"                   :(HELM,1,  40,    0.1,  30,  CLTH,( 2,  0,  0,  0,  5,  10, 5,), ),
"skin mask"                 :(HELM,1,  180,   1.25, 20,  FLSH,( 1,  0,  0,  -1, 0,  5,  2,), ),
"wood mask"                 :(HELM,1,  10,    1.0,  60,  WOOD,( 1,  1, -3,  -1, -5, 5,  5,), ),
"skull helm"                :(HELM,2,  750,   2.8,  125, BONE,(-3,  2, -6,  -2, 5,  5,  5,), ),
"metal mask"                :(HELM,12, 6000,  2.2,  375, METL,(-3,  3, -3,  -2, 0,  5,  -5,), ),
"metal helm"                :(HELM,14, 8500,  3.0,  600, METL,(-4,  4, -6,  -2, 0,  5,  -10,), ),
"graphene mask"             :(HELM,18, 21850, 0.8,  225, CARB,(-1,  5, -3,  -2, 10, 10, 8,), ),
"graphene helmet"           :(HELM,18, 25450, 1.2,  310, CARB,(-1,  6, -3,  -1, 10, 10, 10,), ),
"space helmet"              :(HELM,15, 51950, 3.5,  50,  CARB,(-4,  1, -12, -1, 15, 25, 5,), ),
"gas mask"                  :(HELM,11, 19450, 2.5,  40,  PLAS,(-2,  1, -3,  -2, 10, 45, 6,), ),
"respirator"                :(HELM,5,  2490,  1.7,  35,  PLAS,(-3,  0, -6,  0,  20, 30, 3,), ),

    }        

WEAPONS = {
# Type              Weapon type
# $$$, KG, Dur      Value, mass, durability
# Cap               Ammo Capacity (for ranged weapons)
# Mat               Material
# Ac                Accuracy (for ranged weapons or for throwing weapons),
# At,Dm             Attack, Damage,
# DV,AV,            Dodge Value, Armor Value,
# Asp,Msp           Attack Speed, Move Speed,
# FIR,BIO,          FIRE damage, BIO damage
# Ammo              Ammunition / Fuel required to use weapon
    
           ##------- Type, $$$$, KG,  Dur, Cap,Mat, (Ac,At,Dm, DV, AV, Asp,Msp,ELEM),Ammo,{Misc.Mods},
    # melee weapons
"pocket knife"      :(MEL, 100,  0.2, 120, 0,  METL,(4, 8, 3,   2,  0,  50, 0, PH,),None,(),),
"dagger"            :(MEL, 275,  0.4, 120, 0,  METL,(4, 12,5,   3,  0,  40, 0, PH,),None,(),),
"baton"             :(MEL, 75,   0.75,400, 0,  PLAS,(3, 5, 2,   0,  0,  10,-3, PH,),None,(),),
"staff"             :(MEL, 15,   1.0, 480, 0,  WOOD,(4, 9, 4,   1,  0,  33,-15,PH,),None,(REACH,),),
"cudgel"            :(MEL, 1,    1.5, 680, 0,  WOOD,(2, 3, 10,  -3, 0, -33,-12,PH,),None,(),),
"axe"               :(MEL, 120,  1.25,350, 0,  METL,(3, 5, 12,  -1, 0, -25,-12,PH,),None,(),),
"sword"             :(MEL, 850,  1.25,260, 0,  METL,(4, 12,6,   4,  0,  25,-6, PH,),None,(),),
"spear"             :(MEL, 150,  1.5, 325, 0,  METL,(6, 16,6,   -2, 0,  33,-18,PH,),None,(REACH,),),
    # heavy weapons
"shitstormer"       :(HEVY,1090, 2.5, 220, 50, PLAS,(6, 25,25, -4,  0, -25,-15,BI,),A_HAZM,(),),
"raingun"           :(HEVY,1990, 2.85,175, 50, PLAS,(5, 26,40, -5,  0,  0, -18,CH,),A_ACID,(),),
"supersoaker 9000"  :(HEVY,6750, 3.5, 100, 100,PLAS,(4, 32,1,  -10, 0, -10,-18,None,),A_FLUID,(),),
    # guns
"musket"            :(GUN, 1100, 2.5, 120, 1,  METL,(8, 14,8,  -3,  0, -45,-12,PH,),A_BALL,(),),
"flintlock pistol"  :(GUN, 1750, 1.3, 150, 1,  METL,(8, 10,4,   0,  0,  0, -3, PH,),A_BALL,(),),
"revolver"          :(GUN, 3990, 1.0, 360, 6,  METL,(12,12,6,   0,  0,  0, -3, PH,),A_BULL,(),),
"rifle"             :(GUN, 4575, 2.2, 280, 1,  METL,(20,20,12, -3,  0, -35,-12,PH,),A_BULL,(),),
"shotgun"           :(GUN, 2350, 2.0, 325, 1,  METL,(6, 6, 3,  -2,  0, -25,-9, PH,),A_SHOT,(),),
    # energy weapons
"battery gun"       :(ENER,3250, 4.20,175, 20, PLAS,(5, 40,70, -7,  0, -60,-24,EL,),A_ELEC,(),),
    # heavy weapons
}
'''
"spring-blade"      :(MEL, 9660, 2.8, 150, CARB,(0, 0,  8, 22, -2,  0, -60,-15,PH,),A_ELEC,),
"buzz saw"          :(MEL, 7500, 3.5, 480, METL,(0, 0,  15,5,  -5,  0,  66,-18,PH,),A_ELEC,),
"plasma sword"      :(MEL, 84490,2.0, 250, METL,(0, 0,  11,100,-2,  0, -40,-12,FI,),A_OIL,),
'''



#non-weapon gear
#pass in the name of a gear item
#   quality = 0 to 1. Determines starting condition of the item
def create_gear(name,x,y,quality):
    gData = GEAR[name]
    i =0; j = 0;
    g = thing.Thing()
    g.name = name
    g.x = x
    g.y = y
    g.type = gData[i]; i+=1;
    g.value = gData[i]; i+=1;
    g.mass = gData[i]; i+=1;
    g.hpmax = gData[i]; i+=1;
    g.material = gData[i]; i+=1;
    g.stats.dfn = gData[i][j]; j+=1;
    g.stats.arm = gData[i][j]; j+=1;
    g.stats.msp = gData[i][j]; j+=1;
    g.stats.sight = gData[i][j]; j+=1;
    g.stats.resbio = gData[i][j]; j+=1;
    g.stats.resfire = gData[i][j]; j+=1;
    g.stats.reselec = gData[i][j]; j+=1;

    g.color = COL['white']
    g.mask = g.type    
    
    rog.make(g,CANEQUIP)
    if g.type == ARMR:
        g.equipType = EQ_BODY
    elif g.type == HELM:
        g.equipType = EQ_HEAD
    elif g.type == BACK:
        g.equipType = EQ_BACK
    
    #item resistances based on material

    return g
#


def create_weapon(name, x,y):
    weap = thing.Thing()
    weap.name = name
    weap.x = x
    weap.y = y

    data = WEAPONS[name]
    j = 0
    weap.name       = name
    weap.type       = data[j]; j+=1;
    weap.mask       = weap.type
    weap.value      = data[j]; j+=1;    # $$$
    weap.stats.mass = data[j]; j+=1;    # kg
    weap.stats.hpmax= data[j]; j+=1;    # durability
    weap.capacity   = data[j]; j+=1;
    weap.material   = data[j]; j+=1;
    weap.statMods   = {}        # stat modifiers for equipping
    if data[j][0]:  weap.statMods.update({'range':data[j][0]})
    if data[j][1]:  weap.statMods.update({'atk':data[j][1]})
    if data[j][2]:  weap.statMods.update({'dmg':data[j][2]})
    if data[j][3]:  weap.statMods.update({'dfn':data[j][3]})
    if data[j][4]:  weap.statMods.update({'arm':data[j][4]})
    if data[j][5]:  weap.statMods.update({'asp':data[j][5]})
    if data[j][6]:  weap.statMods.update({'msp':data[j][6]})
    if data[j][7]:  weap.statMods.update({'element':data[j][7]})
    j+=1
    weap.ammoType   = data[j]; j+=1;
    mods = data[j]; j+=1;
    #for mod in data[j]:
    #    weap.mods.append(mod)
    #j+=1;
    
    weap.color      = COL['white']
    weap.equipType  = EQ_MAINHAND
    rog.make(weap,CANEQUIP)

    return weap
#
























