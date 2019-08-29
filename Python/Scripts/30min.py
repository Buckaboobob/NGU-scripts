"""24-hour rebirth script"""

# Challenges
from challenges.basic import Basic
from challenges.level import Level

# Helper classes
from classes.challenge import Challenge
from classes.features import Features
from classes.inputs import Inputs
from classes.navigation import Navigation
from classes.stats import Stats, EstimateRate, Tracker
from classes.upgrade import UpgradeEM
from classes.window import Window
from classes.ngui import NGUI

import coordinates as coords
import time
import datetime


def speedrun(duration, f):
    """Start a speedrun.

    Keyword arguments
    duration -- duration in minutes to run
    f -- feature object
    """
    time.sleep(1)
    rt = f.rt_to_seconds()
    end = (duration * 60) + 1
    itopod_advance = False
    f.nuke()
#    tracker.get_tm_allocated(self)
#    print("Energy Allocated: " + tracker.mystats['TM'][0])
#    print("Magic Allocated: " + tracker.mystats['TM'][1])

    if rt < 60:
        f.loadout(1)  # Gold drop equipment
        f.adventure(highest=True)
        t_end = time.time() + 60
        while time.time() < t_end and rt < end - 20:
            for x in range(1, 8, 1):
                f.time_machine(1e6, magic=True)
                time.sleep(0.5)
            f.augments({"CI": 0.7, "ML": 0.3}, 1.5e6)
        f.loadout(3)  # Bar/power equimpent
#        tracker.get_tm_allocated()
#        print("Energy Allocated: " + tracker.mystats['TM'][0])
#        print("Magic Allocated: " + tracker.mystats['TM'][1])
        f.adventure(itopod=True, itopodauto=True)
        f.augments({"CI": 0.7, "ML": 0.3},1.5e6)
        time.sleep(10)
        f.blood_magic(3, reverse=True)
        f.wandoos(True)

    while rt < end - 300:
        t_end = time.time() + 60
        my_interval = 0
        while time.time() < t_end and rt < end - 300:
            my_interval += 1
            f.wandoos(True)
            time.sleep(0.5)
            f.augments({"CI": 0.9, "ML": 0.1}, f.get_idle_cap(1))
            if my_interval == 8:
                f.blood_magic(3, reverse=True)
#        f.gold_diggers([3])
        rt = f.rt = f.rt_to_seconds()
    if rt > end - 300:
        f.send_string("r")
        f.send_string("t")
        f.blood_magic(3, reverse=True)
        f.augments({"CI": 0.3, "ML": 0.7}, f.get_idle_cap(1))
        f.gold_diggers([3])
        f.fight()
    while rt < end + 30:
        time.sleep(1)
        f.fight()
        rt = f.rt_to_seconds()

#            try:
#                f.assign_ngu(f.get_idle_cap(2), [x for x in range(1, 10)])
#                f.cap_ngu([x for x in range(1, 10)])
#                f.assign_ngu(f.get_idle_cap(1), [x for x in range(1, 8)], True)
#                f.cap_ngu([x for x in range(1, 8)], True)
#                if r3unlocked:
#                    f.hacks(list(range(1, 16)), f.get_idle_cap(3))
#            except ValueError:
#                print("couldn't assign e/m to NGUs")
#            time.sleep(0.5)
#        if rt > 90 and not itopod_advance:
#            f.adventure(itopod=True, itopodauto=True)
#            itopod_advance = True
        rt = f.rt = f.rt_to_seconds()
#        print("Time: " + str(datetime.datetime.now()))

    if rt > end:
#        f.nuke()
#        time.sleep(2)
#        f.fight()
        f.pit()
        f.spin()
        f.save_check()
        tracker.progress()
        u.fix_pcb_ratio()
        u.buy()
#        print("Buy!")

        tracker.adjustxp()
#    print("Going into Sleep till 30 mins up?")
#    print(str(f.rt_to_seconds()) + " < end")

    if rt > end:
        f.do_rebirth()
        time.sleep(1)
        rt = f.rt_to_seconds()
    return


w = Window()
i = Inputs()
nav = Navigation()
feature = Features()
ngui = NGUI(nav)


Window.x, Window.y = i.pixel_search(coords.TOP_LEFT_COLOR, 0, 0, 400, 600)
nav.menu("inventory")

u = UpgradeEM(10000, 10000, 2, 2, 1)
r3unlocked = False

print(f"Top left found at: {w.x}, {w.y}")

tracker = Tracker(30)

while True:  # main loop
    speedrun(30, feature)
    tracker.progress()
