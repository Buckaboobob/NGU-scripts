"""Contains functions for running a no augments challenge."""
from classes.features import Features
import coordinates as coords
import time


class Augment(Features):
    """Contains functions for running a no augments challenge."""

    def normal_rebirth(self, duration):
        """Procedure for first rebirth."""
        diggers = [2, 3, 11, 12]  # Wandoos, stat, blood, exp
        self.nuke()
        time.sleep(2)
        self.fight()
        self.adventure(highest=True)
        self.set_wandoos(1)  # wandoos Meh, use 0 for 98
        self.toggle_auto_spells(drop=False)
        self.gold_diggers(diggers)
        while self.check_pixel_color(*coords.COLOR_TM_LOCKED):
            self.wandoos(True)
            self.nuke()
            time.sleep(2)
            self.fight()
            rb_time = self.get_rebirth_time()
            # return if challenge is completed and rebirth time is above 3 minutes
            if not self.check_challenge():
                return
            if int(rb_time.timestamp.tm_min) >= int(duration):
                self.do_rebirth()
                return
 #           else:
 #               print("Not Returning")
 #               print(str(self.check_challenge()))
 #               print(str(int(rb_time.timestamp.tm_min)))
 #               print(str(duration))

        self.time_machine(self.get_idle_cap(1), magic=True)
#        self.adventure(itopod=True, itopodauto=True)

        while self.check_pixel_color(*coords.COLOR_BM_LOCKED):
            self.adventure(highest=True)
            self.wandoos(True)
            self.time_machine(self.get_idle_cap(1), magic=True)
            self.nuke()
            time.sleep(2)
            self.fight()
            self.gold_diggers(diggers)
            rb_time = self.get_rebirth_time()
            # return if challenge is completed and rebirth time is above 3 minutes
            if not self.check_challenge():
                return
            if int(rb_time.timestamp.tm_min) >= int(duration):
                self.do_rebirth()
                return
#            else:
#                print("Not Returning")
#                print(str(self.check_challenge()))
#                print(str(int(rb_time.timestamp.tm_min)))
#                print(str(duration))

        self.blood_magic(8)
        rb_time = self.get_rebirth_time()
        while int(rb_time.timestamp.tm_min) < duration:
            self.adventure(highest=True)
            self.wandoos(True)
            self.time_machine(self.get_idle_cap(1), magic=True)
            self.nuke()
            self.fight()
            time.sleep(2)
            self.gold_diggers(diggers)
            rb_time = self.get_rebirth_time()
            # return if challenge is completed and rebirth time is above 3 minutes
            if not self.check_challenge():
                return
            if int(rb_time.timestamp.tm_min) >= int(duration):
                self.do_rebirth()
                return
#            else:
#                print("Not Returning")
#                print(str(self.check_challenge()))
#                print(str(int(rb_time.timestamp.tm_min)))
#                print(str(duration))

        self.do_rebirth()

    def start(self):
        """Challenge rebirth sequence.

        If you wish to edit the length or sequence of the rebirths; change the for-loop values
        and durations in the self.normal_rebirth(duration) calls."""

        for x in range(1):  # runs 3-minute rebirth 8 times, if we still aren't done move to 7 min
            self.normal_rebirth(3)  # start a run with a 3 minute duration
            if not self.check_challenge():
                return
        for x in range(2):
            self.normal_rebirth(7)
            if not self.check_challenge():
                return
        for x in range(5):
            self.normal_rebirth(12)
            if not self.check_challenge():
                return
        for x in range(5):
            self.normal_rebirth(30)
            if not self.check_challenge():
                return
        return
