"""24-hour rebirth script."""

# Helper classes
from classes.features import Features
from classes.inputs import Inputs
from classes.navigation import Navigation
from classes.window import Window
from classes.ngui import NGUI
import coordinates as coords
import time


def start_procedure(f, rt):
    """Procedure that handles start of rebirth."""
#    f.merge_equipment()#
#    f.boost_equipment()
    f.merge_inventory(5)
#    f.boost_inventory(8)
#    f.boost_cube()
#    print("Sleeping for 600 seconds")
#    time.sleep(300)
#    if f.check_pixel_color(*coords.IS_IDLE):
#        print("toggle off idle")
#        f.click(*coords.ABILITY_IDLE_MODE)
    #print("Waiting 25 seconds")
    #time.sleep(25)
    #print("Finished Waiting")
    f.reclaim_ngu(magic=True)
    f.reclaim_ngu()
    f.pit()
    f.loadout(3)
    f.deactivate_all_diggers()
    f.gold_diggers([9])
    f.YGG_harvest_activate()
    f.deactivate_all_diggers()
    f.gold_diggers([1, 4, 5, 7, 8, 9])
    f.loadout(4)
    f.level_diggers()
    idle_magic = f.get_idle_cap(2)
    idle_energy = f.get_idle_cap(1)
    while any([idle_magic, idle_energy]):
        print("Idle Caps not empty")
        idle_energy = f.get_idle_cap(1)
        if idle_energy != 0:
            print("Reassign NGU Energy")
            #f.assign_ngu(idle_energy, [1, 2, 3, 4, 5, 6, 7])
            f.assign_ngu(idle_energy, [5])
        idle_magic = f.get_idle_cap(2)
        if idle_magic != 0:
            print("Reassign NGU Magic")
            f.assign_ngu(idle_magic, [1, 2], magic=True)
        #            f.blood_magic(7, reverse=True)
        idle_magic = f.get_idle_cap(2)
        idle_energy = f.get_idle_cap(1)
    secs = 60
    print(f"sniping for {secs} Seconds")
    #    time.sleep(secs)
    for _ in range(15):
        f.itopod_snipe(secs)
        if f.check_pixel_color(*coords.IS_IDLE):
            print("Didn't toggle Idle")
        else:
            print("toggle off idle")
            f.click(*coords.ABILITY_IDLE_MODE)
        f.menu("inventory")
        f.boost_equipment()
#        f.boost_inventory(8)
        f.boost_cube()
    print("Done Sniping")

w = Window()
i = Inputs()
nav = Navigation()
feature = Features()
#ngui = NGUI(nav_obj=nav, input_obj=i)
Window.x, Window.y = i.pixel_search(coords.TOP_LEFT_COLOR, 0, 0, 400, 600)
time.sleep(2)
rt = feature.get_rebirth_time()
start_procedure(feature, rt)

while True:
    rt = feature.get_rebirth_time()
    spells = feature.check_spells_ready()
    start_procedure(feature, rt)
#    if spells:  # check if any spells are off CD
#        for spell in spells:
#            feature.cast_spell(spell)
    feature.save_check()
    feature.pit()

#    time.sleep(120)
    print(str(rt))
