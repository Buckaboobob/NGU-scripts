"""24-hour rebirth script."""

# Helper classes
from classes.features import Features
from classes.inputs import Inputs
from classes.navigation import Navigation
from classes.window import Window

import coordinates as coords
import time


def start_procedure(f, rt):
    """Procedure that handles start of rebirth."""
    print("Boosting/Merging")
    nav.menu("inventory")
#    f.merge_equipment()
#    f.merge_inventory(16)
#    f.boost_inventory(6)
#    f.boost_equipment()
#    f.boost_cube()
#    f.reclaim_bm()
    f.reclaim_ngu(magic=True)
    f.reclaim_ngu()
    f.pit()
    f.loadout(3)
    f.gold_diggers([1, 4, 5, 6, 7, 8], deactivate=True)
    f.gold_diggers([9])
    f.YGG_harvest_activate()
    f.level_diggers()
    f.gold_diggers([9], deactivate=True)
    f.gold_diggers([1, 4, 5, 6, 7, 8])
    f.loadout(2)
    time.sleep(30)
    f.loadout(2)
    idle_magic = f.get_idle_cap(2)
    idle_energy = f.get_idle_cap(1)
    while any([idle_magic, idle_energy]):
        print("Idle Caps not empty")
        idle_energy = f.get_idle_cap(1)
        if idle_energy != 0:
            print("Reassign NGU Energy")
            f.assign_ngu(idle_energy,[7])
#            f.assign_ngu(idle_energy, [1, 2, 3, 4, 5, 6, 7])
        idle_magic = f.get_idle_cap(2)
        if idle_magic != 0:
            print("Reassign NGU Magic")
            f.assign_ngu(idle_magic, [7], magic=True)
#            f.blood_magic(7, reverse=True)
        idle_magic = f.get_idle_cap(2)
        idle_energy = f.get_idle_cap(1)
    sp = f.check_spells_ready()
    if sp:  # check if any spells are off CD
        for spell in spells:
            feature.cast_spell(spell)
    nav.menu("inventory")
    secs = 60
    print(f"sniping for {secs} Seconds")
#    time.sleep(secs)
    for _ in range(15):
        time.sleep(secs)
        f.menu("inventory")
#        f.boost_equipment()
        f.boost_inventory(1)
    print("Done Sniping")


w = Window()
i = Inputs()
nav = Navigation()
feature = Features()

Window.x, Window.y = i.pixel_search(coords.TOP_LEFT_COLOR, 0, 0, 400, 600)
nav.menu("inventory")
rt = feature.get_rebirth_time()
start_procedure(feature, rt)

while True:
    rt = feature.get_rebirth_time()
    #    feature.nuke()
    #    feature.gold_diggers([x for x in range(1, 13)])
    #    feature.merge_inventory(8)  # merge uneqipped guffs
    spells = feature.check_spells_ready()
    if spells:  # check if any spells are off CD
        #        feature.reclaim_ngu(True)  # take all magic from magic NGUs
        for spell in spells:
            feature.cast_spell(spell)
    #        feature.reclaim_bm()
    #        feature.assign_ngu(feature.get_idle_cap(True), [x for x in range(1, 8)], True)
    #        feature.toggle_auto_spells()  # retoggle autospells

    #    if 1 > 0:  # rebirth is at >24 hours
    #        print(f"rebirthing at {rt}")  # debug
    #        feature.nuke()
    #        feature.spin()
    #        feature.deactivate_all_diggers()
    #        feature.ygg(equip=1)  # harvest with equipment set 1
    #        feature.ygg(eat_all=True)
    #        feature.level_diggers()  # level all diggers
    #        feature.do_rebirth()
    #        time.sleep(3)
    #        rt = feature.get_rebirth_time()
    #        start_procedure(feature, rt)
    #    else:
    #    feature.ygg()
    feature.save_check()

    start_procedure(feature, rt)
#    time.sleep(300)
#    print(str(rt))
#        if rt.timestamp.tm_hour <= 12:  # quests for first 12 hours
#            feature.boost_cube()
#            feature.questing()
#        else:  # after hour 12, do itopod in 5-minute intervals
#            feature.itopod_snipe(300)
#            feature.boost_cube()
