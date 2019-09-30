"""Contains functions for running a 100 level challenge."""
from classes.features import Features
import coordinates as coords
import time

class Level(Features):
    """Contains functions for running a 100 level challenge.

    IMPORTANT

    Set target level for energy buster to 67 and charge shot to 33.
    Disable "Advance Energy" in augments
    Disable beards if you cap ultra fast.

    """
    def speedrun(self, duration):
        """Procedure for first rebirth in a 100LC."""
        self.nuke()
        time.sleep(2)
        self.fight()
        diggers = [3]
        self.adventure(highest=True)
        current_boss = int(self.get_current_boss())
        if current_boss < 28:
            self.augments({"CI": 1}, coords.INPUT_MAX)
        if current_boss > 48:
            self.adventure(highest=True)
            self.augments({"EB": 0.66, "CS": 0.34}, self.get_idle_cap(1))
        else:
            self.augments({"EB": 1}, coords.INPUT_MAX)
        if not self.check_pixel_color(*coords.COLOR_TM_LOCKED):
            self.time_machine(1e6, magic=True)
            self.gold_diggers(diggers)
        rb_time = self.get_rebirth_time()
        while int(rb_time.timestamp.tm_min) < duration:
            self.augments({"EB": 0.66, "CS": 0.34}, self.get_idle_cap(1))
            self.nuke()
            self.fight()
            current_boss = int(self.get_current_boss())
            if current_boss == 38:
                self.adventure(highest=True)
            self.gold_diggers(diggers)
            rb_time = self.get_rebirth_time()
            if not self.check_challenge() and rb_time.timestamp.tm_min >= 3:
                return
        if not self.check_challenge() and rb_time.timestamp.tm_min >= 3:
            return
        self.do_rebirth()
        return

    def start(self):
        """Handle LC run."""
        for x in range(5):
            self.speedrun(4)
            if not self.check_challenge():
                return
        for x in range(5):
            self.speedrun(7)
            if not self.check_challenge():
                return
        for x in range(5):
            self.speedrun(12)
            if not self.check_challenge():
                return
        for x in range(5):
            self.speedrun(60)
            if not self.check_challenge():
                return
