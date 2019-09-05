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
    f.merge_equipment()
    f.boost_equipment()
    f.merge_inventory(7)
    f.boost_inventory(1)
    f.boost_cube()
    print("Sniping")
    nav.menu("adventure")
    f.adventure(0, highest=False)
    feature.snipe(16, 5, once=False, bosses=True, manual=True)
    print("Finished Snipe")
    f.adventure(0, highest=False)
    if f.check_pixel_color(*coords.IS_IDLE):
        print("toggle off idle")
        f.click(*coords.ABILITY_IDLE_MODE)
    #print("Waiting 25 seconds")
    #time.sleep(25)
    #print("Finished Waiting")
    pass

w = Window()
i = Inputs()
nav = Navigation()
feature = Features()
ngui = NGUI(nav_obj=nav, input_obj=i)
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
