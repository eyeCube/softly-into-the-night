'''
    stuff.py
    inanimate tts to populate the world
'''

from const import *
import rogue as rog
import thing
import dice
from colors import COLORS as COL


STUFF={
#flag       :  name             type     material, color,  Lo,kg,  solid,push?,script,
THG.GORE    : ("hunk of meat",  T_GORE, MAT_FLESH, 'red',  1, 1,   False,False,_food_meal,),
THG.LOG     : ("log",           T_LOG,  MAT_WOOD, 'brown',250,20,  False,False,None,),
THG.WOOD    : ("wood",          T_WOOD, MAT_WOOD, 'brown', 50,2,   False,False,None,),
THG.BOX     : ("crate",         T_BOX,  MAT_WOOD, 'brown',100,10,  True,True,  _boxOfItems1,),
THG.GRAVE   : ("grave",         T_GRAVE,MAT_STONE,'silver',100,200,True,False, None,),
THG.BIGPOT  : ("cauldron",      T_POT,  MAT_METAL,'metal', 500,100,True,True, _bigFluidContainer,),
THG.STILL   : ("still",         T_STILL,MAT_METAL,'metal', 20, 100,True,False, _still,),
    }


#create a thing from STUFF; does not register thing
def create(x,y,ID):
    name,typ,mat,fgcol,lo,kg,solid,push,script = STUFF[ID]
    tt = thing.Thing(x,y, _type=typ,name=name,color=COL[fgcol])
    tt.mass = kg
    tt.material=mat
    if lo: hp(tt, lo)
    tt.isSolid = solid
    if push: make(tt, CANPUSH)
    #_applyResistancesFromMaterial(tt, mat)
    return tt



#quick functions for multiple types of objects:
def hp(tt, value): #give a Thing a specified amount of HP and fully heal them
    tt.stats.hpmax=value; rog.givehp(tt);
#give a random number of items to the inventory of Thing tt
    #func is a function to build the items
    #_min is minimum number of items possible to give
    #_max is maximum "
def giveRandom(tt, func, _min, _max):
    for ii in range((_min - 1) + dice.roll(_max - (_min - 1))):
        item = func()
        rog.give(tt, item)

#conversion functions:
# convert things into specific types of things by giving them certain data
def _edible(tt, nutrition):
    rog.make(tt,EDIBLE)
    tt.nutrition=nutrition
def _food_poison(tt):
    _edible(tt, RATIONFOOD)
    rog.make(tt,SICK) #makes you sick when you eat it
def _food_ration(tt):
    _edible(tt, RATIONFOOD)
def _food_serving(tt):
    _edible(tt, RATIONFOOD*3)
def _food_meal(tt):
    _edible(tt, RATIONFOOD*9)
def _food_bigMeal(tt):
    _edible(tt, RATIONFOOD*18)
def _fluidContainer(tt):
    rog.init_fluidContainer(tt, 20)
def _bigFluidContainer(tt):
    rog.init_fluidContainer(tt, 100)
def _boxOfItems1(tt):
    rog.init_inventory(tt, 100)
    #newt=
    #rog.give(tt, newt)
    









'''
#gibs
def gore(x,y):
    tt = thing.Thing(x,y,_type=chr(T_GORE),name='hunk of meat',
                     color=COL['red'])
    tt.mass=1
    hp(tt, 1)
    rog.register_inanimate(tt)
    return tt

#wood
def sawdust(x,y):
    tt=thing.Thing(x,y,_type=chr(T_DUST),name="sawdust",
                   color=COL['brown'],material=MAT_SAWDUST)
    tt.mass=0.5
    hp(tt, 1)
    rog.register_inanimate(tt)
    return tt
def wood(x,y):
    tt=thing.Thing(x,y,_type=chr(T_WOOD),name="wood",
                   color=COL['brown'],material=MAT_WOOD)
    tt.mass=2
    hp(tt, 10)
    rog.register_inanimate(tt)
    return tt
def log(x,y):
    tt=thing.Thing(x,y,_type=chr(T_LOG),name="log",
                   color=COL['brown'],material=MAT_WOOD)
    tt.mass=20
    hp(tt, 100)
    rog.register_inanimate(tt)
    return tt

#flora
def tree(x,y):
    tt=thing.Thing(x,y,_type=chr(T_TREE),name="tree",
                   color=COL['green'],material=MAT_WOOD)
    tt.mass=200
    hp(tt, 30)
    rog.init_inventory(tt)
    giveRandom(tt, wood, 1, 6)
    rog.register_inanimate(tt)
    return tt
def corpseShroom(x,y):
    tt=thing.Thing(x,y,_type=chr(T_FUNGUS),name="corpiscle",
                   color=COL['red'],material=MAT_FUNGUS)
    tt.mass=2
    hp(tt, 1)
    _food(tt, 10)
    rog.register_inanimate(tt)
    return tt

#containers
def jug(x,y):
    tt=thing.Thing(x,y,_type=chr(T_BOTTLE),name="empty jug",
                   color=COL['brown'],material=MAT_GLASS)
    tt.mass=1
    hp(tt, 1)
    rog.init_fluidContainer(tt, 10)
    rog.register_inanimate(tt)
    return tt
'''









