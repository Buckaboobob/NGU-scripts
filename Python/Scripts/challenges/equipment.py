"""Contains functions for running a basic challenge."""
from classes.features import Features
import coordinates as coords
import time

class Equipment(Features):
    """Contains functions for running a basic challenge."""

    def speedrun(self, duration):
        """Start a speedrun.

        Keyword arguments
        duration -- duration in minutes to run
        f -- feature object
        """
        diggers = [2, 3, 11, 12]
        self.nuke()
        time.sleep(2)
        self.fight()
        self.adventure(highest=True)
        time.sleep(2)
        rb_time = self.get_rebirth_time()
        while int(rb_time.timestamp.tm_min) < duration:
            self.adventure(highest=True)
            if not self.check_pixel_color(*coords.COLOR_TM_LOCKED):
                self.time_machine(10e6, magic=True)
            self.gold_diggers(diggers)
            self.wandoos(True)
            current_boss = int(self.get_current_boss())
            if current_boss < 28:
                self.augments(({"SS": 0.3, "MI": 0.3, "CI": 0.3}), 1e6)
            else:
                self.augments({"MI": 0.5, "DTMT": 0.5}, coords.INPUT_MAX)
            if not self.check_pixel_color(*coords.COLOR_BM_LOCKED):
                self.blood_magic(6)
            self.nuke()
            rb_time = self.get_rebirth_time()
        self.pit()
        self.spin()
        return

    def start(self):
        """Challenge rebirth sequence.

        If you wish to edit the length or sequence of the rebirths; change the for-loop values
        and durations in the self.speedrun(duration) calls."""
        self.set_wandoos(1)  # wandoos 98, use 1 for meh

        for x in range(3):
            self.speedrun(3)
            if not self.check_challenge():
                return
            self.do_rebirth()
        for x in range(5):
            self.speedrun(7)
            if not self.check_challenge():
                return
            self.do_rebirth()
        for x in range(5):
            self.speedrun(12)
            if not self.check_challenge():
                return
            self.do_rebirth()
        for x in range(5):
            self.speedrun(60)
            if not self.check_challenge():
                return
            self.do_rebirth()
        return
