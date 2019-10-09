"""Questing Script."""

# Helper classes
from classes.features import Features
from classes.window import Window

import coordinates as coords

w = Window()
feature = Features()

Window.x, Window.y = feature.pixel_search(coords.TOP_LEFT_COLOR, 0, 0, 400, 600)
feature.menu("inventory")

print(f"Top left found at: {w.x}, {w.y}")

choice = ""
answers = {"y": True, "ye": True, "yes": True, "n": False, "no": False}
print("If you currently have an active quest that either is minor or has been subcontracted, consider skipping it before starting if you intend to use butter")
while choice not in answers:
    choice = input("Use butter for major quests? y/n: ").lower()

while True:  # main loop
    text = feature.get_quest_text()
    majors = feature.get_available_majors()
    if majors == 0 and (coords.QUESTING_MINOR_QUEST in text.lower() or coords.QUESTING_NO_QUEST_ACTIVE in text.lower()):
        feature.questing(major=True)
    else:
        if not feature.check_pixel_color(*coords.COLOR_QUESTING_USE_MAJOR):
            feature.click(*coords.QUESTING_USE_MAJOR)
        feature.questing(butter=answers[choice])
    feature.reclaim_ngu(magic=True)
    feature.reclaim_ngu()
    feature.pit()
    feature.loadout(3)
    feature.deactivate_all_diggers()
    feature.gold_diggers([9])
    feature.YGG_harvest_activate()
    feature.deactivate_all_diggers()
    feature.gold_diggers([1, 5, 6, 7, 8, 10])
    feature.loadout(4)
    idle_magic = feature.get_idle_cap(2)
    idle_energy = feature.get_idle_cap(1)
    while any([idle_magic, idle_energy]):
        print("Idle Caps not empty")
        idle_energy = feature.get_idle_cap(1)
        if idle_energy != 0:
            print("Reassign NGU Energy")
            feature.assign_ngu(idle_energy, [1, 2, 3, 4, 5, 6, 7])
        idle_magic = feature.get_idle_cap(2)
        if idle_magic != 0:
            print("Reassign NGU Magic")
            feature.assign_ngu(idle_magic, [6], magic=True)
        #            f.blood_magic(7, reverse=True)
        idle_magic = feature.get_idle_cap(2)
        idle_energy = feature.get_idle_cap(1)
