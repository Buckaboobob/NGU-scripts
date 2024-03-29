"""Buys things for exp."""
from classes.stats import Stats, Tracker
import coordinates as coords
import usersettings as userset
import time
# TODO replace ngucon with coordinates
import math


class UpgradeEM(Stats):
    """Buys things for exp."""

    def __init__(self, ecap, mcap, ebar, mbar, e2m_ratio, report=False):
        """Example: Upgrade(37500, 37500, 2, 1).

        This will result in a 1:37500:2 ratio for energy and 1:37500:1 for
        magic. i.e. 1 power, 37500 ecap and 2 ebars.

        Keyword arguments:

        ecap -- The amount of energy cap in the ratio. Must be over 10000 and
                divisible by 250.
        mcap -- The amount of magic cap in the ratio. Must be over 10000 and
                divisible by 250.
        ebar -- the amount of energy bars to buy in relation to power
        mbar -- the amount of magic bars to buy in relation to power.
        e2m_ratio -- The amount of exp to spend in energy in relation to magic.
                     a value of 5 will buy 5 times more upgrades in energy than
                     in magic, maintaining a 5:1 E:M ratio.
        """
        self.ecap = ecap
        self.mcap = mcap
        self.ebar = ebar
        self.mbar = mbar
        self.e2m_ratio = e2m_ratio
        self.report = report

    def fix_pcb_ratio(self):
        """ Fix Power Cap Bar resource ratio
                Currently the ratio is hardcoded just below
                Only works with Energy and Magic as I don't have R yet"""
        ratio = [1, 37500, 1]
        self.exp()
        self.set_value_with_ocr("XP")
        if Stats.OCR_failed:
            print('OCR failed, exiting upgrade routine.')
            return
        try:
            current_exp = Stats.xp
            print("I Have {} to spend".format(str(current_exp)))

            e_base_pow = float(self.ocr(*coords.OCR_POW).strip().replace(',', ''))
            e_base_cap = float(self.ocr(*coords.OCR_CAP).strip().replace(',', ''))
            e_base_bar = float(self.ocr(*coords.OCR_BAR).strip().replace(',', ''))
            print("Energy pow({}) cap({}) bar({})".format(str(e_base_pow), str(e_base_cap), str(e_base_bar)))
            self.exp_magic()
            m_base_pow = float(self.ocr(*coords.OCR_POW).strip().replace(',', ''))
            m_base_cap = float(self.ocr(*coords.OCR_CAP).strip().replace(',', ''))
            m_base_bar = float(self.ocr(*coords.OCR_BAR).strip().replace(',', ''))
            print("Magic pow({}) cap({}) bar({})".format(str(m_base_pow), str(m_base_cap), str(m_base_bar)))
            my_e_cap = int(e_base_cap / ratio[1])
            my_m_cap = int(m_base_cap / ratio[1])

            if m_base_bar < (my_m_cap * ratio[2]):
                need_m_base_bar = (my_m_cap * ratio[2]) - m_base_bar
                print("Magic Bars is Below Ratio by {}".format(str(need_m_base_bar)))
                can_buy_mbar = math.trunc(current_exp / coords.MBAR_COST)
                print("I can buy {} Magic Bars".format(str(can_buy_mbar)))
                self.exp_magic()
                time.sleep(userset.MEDIUM_SLEEP)
                self.click(*coords.EM_BAR_BOX)
                self.send_string(str(can_buy_mbar))
                time.sleep(userset.MEDIUM_SLEEP)
                self.click(*coords.EM_BAR_BUY)
                return

            if e_base_bar < (my_e_cap * ratio[2]):
                need_e_base_bar = (my_e_cap * ratio[2]) - e_base_bar
                print("Energy Bars is Below Ratio by " + str(need_e_base_bar))
                can_buy_ebar = math.trunc(current_exp / coords.EBAR_COST)
                print("I can buy " + str(can_buy_ebar) + " Energy Bars")
                self.exp()
                time.sleep(userset.MEDIUM_SLEEP)
                self.click(*coords.EM_BAR_BOX)
                self.send_string(str(can_buy_ebar))
                time.sleep(userset.MEDIUM_SLEEP)
                self.click(*coords.EM_BAR_BUY)
                return

            if e_base_pow < (my_e_cap * ratio[0]):
                need_e_base_pow = int(my_e_cap * ratio[0]) - e_base_pow
                print("Energy Power is Below Ratio by " + str(need_e_base_pow))
                can_buy_epow = math.trunc(current_exp / coords.EPOWER_COST)
                print("I can buy " + str(can_buy_epow) + " Energy Power")
                self.exp()
                time.sleep(userset.MEDIUM_SLEEP)
                self.click(*coords.EM_POW_BOX)
                self.send_string(str(can_buy_epow))
                time.sleep(userset.MEDIUM_SLEEP)
                self.click(*coords.EM_POW_BUY)
                return

            if m_base_pow < (my_m_cap * ratio[0]):
                need_m_base_pow = (my_m_cap * ratio[0]) - m_base_pow
                print("Magic Power is Below Ratio by " + str(need_m_base_pow))
                can_buy_mpow = math.trunc(current_exp / coords.MPOWER_COST)
                print("I can buy " + str(can_buy_mpow) + " Magic Power")
                self.exp_magic()
                time.sleep(userset.MEDIUM_SLEEP)
                self.click(*coords.EM_POW_BOX)
                self.send_string(str(can_buy_mpow))
                time.sleep(userset.MEDIUM_SLEEP)
                self.click(*coords.EM_POW_BUY)
                return



        except:
            print("Something went wrong... not fixing ratio's")

        return


    def buy(self):
        """Buy upgrades for both energy and magic.

        Requires the confirmation popup button for EXP purchases in settings
        to be turned OFF.

        This uses all available exp, so use with caution.
        """
        if self.ecap < 10000 or self.ecap % 250 != 0:
            print("Ecap value not divisible by 250 or lower than 10000, not" +
                  " spending exp.")
            return
        if self.mcap < 10000 or self.mcap % 250 != 0:
            print("Mcap value not divisible by 250 or lower than 10000, not" +
                  " spending exp.")
            return

        self.set_value_with_ocr("XP")
        if Stats.OCR_failed:
            print('OCR failed, exiting upgrade routine.')
            return

        current_exp = Stats.xp

        e_cost = coords.EPOWER_COST + coords.ECAP_COST * self.ecap + (
                 coords.EBAR_COST * self.ebar)

        m_cost = coords.MPOWER_COST + coords.MCAP_COST * self.mcap + (
                 coords.MBAR_COST * self.mbar)

        total_price = m_cost + self.e2m_ratio * e_cost

        """Skip upgrading if we don't have enough exp to buy at least one
        complete set of upgrades, in order to maintain our perfect ratios :)"""

        if total_price > current_exp:
            if self.report:
                print("No XP Upgrade :{:^8} of {:^8}".format(self.human_format(current_exp),self.human_format(total_price)))
            return

        amount = int(current_exp // total_price)

        e_power = amount * self.e2m_ratio
        e_cap = amount * self.ecap * self.e2m_ratio
        e_bars = amount * self.ebar * self.e2m_ratio
        m_power = amount
        m_cap = amount * self.mcap
        m_bars = amount * self.mbar

        self.exp()

        self.click(*coords.EM_POW_BOX)
        self.send_string(str(e_power))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_CAP_BOX)
        self.send_string(str(e_cap))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_BAR_BOX)
        self.send_string(str(e_bars))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_POW_BUY)
        self.click(*coords.EM_CAP_BUY)
        self.click(*coords.EM_BAR_BUY)

        self.exp_magic()

        self.click(*coords.EM_POW_BOX)
        self.send_string(str(m_power))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_CAP_BOX)
        self.send_string(str(m_cap))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_BAR_BOX)
        self.send_string(str(m_bars))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_POW_BUY)
        self.click(*coords.EM_CAP_BUY)
        self.click(*coords.EM_BAR_BUY)

        self.set_value_with_ocr("XP")

        total_spent = coords.EPOWER_COST * e_power + coords.ECAP_COST * e_cap + coords.EBAR_COST * e_bars
        total_spent += coords.MPOWER_COST * m_power + coords.MCAP_COST * m_cap + coords.MBAR_COST * m_bars

        if self.report:
            print("Spent XP:{:^8}".format(self.human_format(total_spent)))
            print("Energy | Pow:{:^8}{:^3}Cap:{:^8}{:^3}Bar:{:^8}{:^3}Magic | Pow:{:^8}{:^3}Cap:{:^8}{:^3}Bar:{:^8}".format(
                self.human_format(e_power), "|",
                self.human_format(e_cap), "|",
                self.human_format(e_bars), "|",
                self.human_format(m_power), "|",
                self.human_format(m_cap), "|",
                self.human_format(m_bars)))

    def human_format(self, num):
        num = float('{:.3g}'.format(num))
        if num > 1e14:
            return
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


class UpgradeAdventure(Stats):
    """Buys things for exp."""

    def __init__(self, power, toughness, health, regen, ratio, report=False):
        self.power = power
        self.toughness = toughness
        self.health = health
        self.regen = regen
        self.ratio = ratio
        self.report = report

    def buy(self):
        """Buy upgrades for power, toughness, health and regen

        Requires the confirmation popup button for EXP purchases in settings
        to be turned OFF.

        This uses all available exp, so use with caution.
        """
        self.set_value_with_ocr("XP")

        if Stats.OCR_failed:
            print('OCR failed, exiting upgrade routine.')
            return

        current_exp = Stats.xp

        total_price = (coords.APOWER_COST * self.power * self.ratio)
        total_price += (coords.ATOUGHNESS_COST * self.toughness * self.ratio)
        total_price += (coords.AHEALTH_COST * self.health * 10)
        total_price += math.floor(coords.AREGEN_COST * self.regen / 10)

        """Skip upgrading if we don't have enough exp to buy at least one
        complete set of upgrades, in order to maintain our perfect ratios :)"""

        if total_price > current_exp:
            if self.report:
                print("No XP Upgrade :{:^8} of {:^8}".format(self.human_format(current_exp), self.human_format(total_price)))
            return

        amount = int(current_exp // total_price)

        a_power = amount * self.ratio
        a_toughness = amount * self.ratio
        a_health = amount * 10
        a_regen = math.floor(amount / 10)
        if a_regen < 1:
            a_regen = 1.0

        self.exp_adventure()

        self.click(*coords.EM_ADV_BOX)
        self.send_string(str(a_power))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_POW_BOX)
        self.send_string(str(a_toughness))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_CAP_BOX)
        self.send_string(str(a_health))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_BAR_BOX)
        self.send_string(str(a_regen))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_ADV_BUT)
        self.click(*coords.EM_POW_BUY)
        self.click(*coords.EM_CAP_BUY)
        self.click(*coords.EM_BAR_BUY)

        self.set_value_with_ocr("XP")

        total_spent = coords.APOWER_COST * a_power
        total_spent += coords.ATOUGHNESS_COST * a_toughness
        total_spent += coords.AHEALTH_COST * a_health
        total_spent += coords.AREGEN_COST * a_regen

        if self.report:
            print("Spent XP:{:^8}".format(self.human_format(total_spent)))
            print("Power:{:^8}{:^3} Defense:{:^8}{:^3} Health:{:^8}{:^3} Regen:{:^8}".format(
                self.human_format(a_power), "|",
                self.human_format(a_toughness), "|",
                self.human_format(a_health), "|",
                self.human_format(a_regen)))

    def human_format(self, num):
        num = float('{:.3g}'.format(num))
        if num > 1e14:
            return
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


class UpgradeRich(Stats):
    """Buys things for exp."""

    def __init__(self, attack, defense, report=False):
        self.attack = attack
        self.defense = defense
        self.report = report

    def buy(self):
        """Buy upgrades for both attack and defense

        Requires the confirmation popup button for EXP purchases in settings
        to be turned OFF.

        This uses all available exp, so use with caution.
        """
        self.set_value_with_ocr("XP")

        if Stats.OCR_failed:
            print('OCR failed, exiting upgrade routine.')
            return

        current_exp = Stats.xp

        if current_exp < 1000:
            return

        total_price = (coords.RATTACK_COST * self.attack)
        total_price += (coords.RDEFENSE_COST * self.defense)

        """Skip upgrading if we don't have enough exp to buy at least one
        complete set of upgrades, in order to maintain our perfect ratios :)"""

        if total_price > current_exp:
            if self.report:
                print("No XP Upgrade :{:^8} of {:^8}".format(self.human_format(current_exp), self.human_format(total_price)))
            return

        amount = int(current_exp // total_price)

        a_attack = amount * self.attack
        a_defense = amount * self.defense

        self.exp_rich()

        self.click(*coords.EM_ADV_BOX)
        self.send_string(str(a_attack))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_ADV_BOX)
        self.send_string(str(a_defense))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_ADV_BOX)
        self.click(*coords.EM_ADV_BOX)

        self.set_value_with_ocr("XP")

        total_spent = coords.RATTACK_COST * a_attack
        total_spent += coords.RDEFENSE_COST * a_defense

        if self.report:
            print("Spent XP:{:^8}{:^3}Attack:{:^8}{:^3}Defense:{:^8}".format(
                self.human_format(total_spent), "|",
                self.human_format(a_attack), "|",
                self.human_format(a_defense)))

    def human_format(self, num):
        num = float('{:.3g}'.format(num))
        if num > 1e14:
            return
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])


class UpgradeHackPower(Stats):
    """Buys things for exp."""

    def __init__(self, hcap, hbar, hpower, report=False):
        """Example: UpgradeHackPower(10000, 1, 1).

        Keyword arguments:

        hcap -- The amount of hack energy in the ratio. Must be over 1000 and divisible by 250 or 0.
        hbar -- The amount of bars
        hpower -- the amount of new power

        """
        self.hcap = hcap
        self.hbar = hbar
        self.hpower = hpower
        self.report = report

    def buy(self):
        """Buy upgrades for hack energy

        Requires the confirmation popup button for EXP purchases in settings
        to be turned OFF.

        This uses all available exp, so use with caution.
        """
        if (self.hcap < 10000 or self.hcap % 250 != 0) and self.hcap != 0:
            print("Ecap value not divisible by 250 or lower than 10000, not" +
                  " spending exp.")
            return

        self.set_value_with_ocr("XP")
        if Stats.OCR_failed:
            print('OCR failed, exiting upgrade routine.')
            return

        current_exp = Stats.xp

        total_price = coords.HPOWER_COST * self.hpower + coords.HCAP_COST * self.hcap + coords.HBAR_COST * self.hbar

        """Skip upgrading if we don't have enough exp to buy at least one
        complete set of upgrades, in order to maintain our perfect ratios :)"""

        if total_price > current_exp:
            if self.report:
                print("No XP Upgrade :{:^8} of {:^8}".format(self.human_format(current_exp),
                                                             self.human_format(total_price)))
            return

        amount = int(current_exp // total_price)

        h_power = amount * self.hpower
        h_cap = amount * self.hcap
        h_bars = amount * self.hbar

        self.exp_hack()

        self.click(*coords.EM_POW_BOX)
        self.send_string(str(h_power))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_CAP_BOX)
        self.send_string(str(h_cap))
        time.sleep(userset.MEDIUM_SLEEP)

        self.click(*coords.EM_BAR_BOX)
        self.send_string(str(h_bars))
        time.sleep(userset.MEDIUM_SLEEP)

        if h_power > 0:
            self.click(*coords.EM_POW_BUY)
        if h_cap > 0:
            self.click(*coords.EM_CAP_BUY)
        if h_bars > 0:
            self.click(*coords.EM_BAR_BUY)

        self.set_value_with_ocr("XP")

        total_spent = coords.HPOWER_COST * h_power + coords.HCAP_COST * h_cap + coords.HBAR_COST * h_bars

        if self.report:
            print("Spent XP:{:^8}".format(self.human_format(total_spent)))
            print("New | Pow:{:^8}{:^3}Cap:{:^8}{:^3}Bar:{:^8}".format(
                self.human_format(h_power), "|",
                self.human_format(h_cap), "|",
                self.human_format(h_bars)))

    def human_format(self, num):
        num = float('{:.3g}'.format(num))
        if num > 1e14:
            return
        magnitude = 0
        while abs(num) >= 1000:
            magnitude += 1
            num /= 1000.0
        return '{}{}'.format('{:f}'.format(num).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][magnitude])
