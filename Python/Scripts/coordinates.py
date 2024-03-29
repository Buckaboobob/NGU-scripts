from collections import namedtuple

Pixel = namedtuple('Pixel', 'x y')
ColorPixel = namedtuple('ColorPixel', Pixel._fields + ('color',))
OCRBox = namedtuple('OCRBox', 'x1 y1 x2 y2')

# COLORS
TOP_LEFT_COLOR = '000408'
SANITY_AUG_SCROLL_COLORS = ["497C9F", "4C81A5", "4C80A4", "497B9E", "457596"]
NGU_BAR_WHITE = "FFFFFF"
NGU_BAR_GRAY = "FAFAFA"

# Here are the colors I found for Dark_Gold_Theme
#     SANITY_AUG_SCROLL_COLORS, # DIFF ['9E7D11', 'B59012', '94760E' '8B7304'] ('C19915' maybe a bugged value))
#     NGU_BAR_WHITE, # 'B4B3B4'
#     NGU_BAR_GRAY, # NOT USED
#     IS_BOSS_CROWN, # SAME BUT OFF BY 1 pixel in x
#     IS_NOT_DEAD, # SAME
#     IS_DEAD, # SAME
#     IS_ITOPOD_ACTIVE, # SAME
#     IS_IDLE, # SAME
#     IS_SAVE_READY, # '68AD68'
#     IS_PIT_READY, # '568E28'
#     IS_SPIN_READY, # 'AD8E28'
#     IS_CHALLENGE_ACTIVE, # SAME
#     COLOR_TM_LOCKED, # '767776'
#     COLOR_BM_LOCKED, # '767776', {'63375E' w/ iron pill}
#     IS_IRON_PILL_READY, #'7E0D71'
#     PLAYER_HEAL_THRESHOLDX # SAME
# ]

INPUT_MAX = 1000000000000000000

# Adventure Offsets
RIGHT_ARROW = Pixel(930, 220)
LEFT_ARROW = Pixel(325, 225)
ITOPOD = Pixel(405, 225)
ITOPOD_PERKS = Pixel(490, 225)
ITOPOD_START = Pixel(630, 200)
ITOPOD_END = Pixel(630, 240)
ITOPOD_ENTER = Pixel(625, 330)
ITOPOD_AUTO = Pixel(710, 215)
HEALTH = Pixel(706, 411)
ADVENTURE_TOOLTIP = Pixel(445, 45)
OCR_AP_KILL_COUNT = OCRBox(470, 115, 740, 145)
# TODO: Rewrite kill_titan
ABILITY_ROW1X = 426
ABILITY_ROW2X = 321
ABILITY_ROW3X = 321
ABILITY_ROW1Y = 113
ABILITY_ROW2Y = 150
ABILITY_ROW3Y = 186

# ROW 1 ABILITIES
ABILITY_IDLE_MODE = Pixel(330, 105)
ABILITY_REGULAR_ATTACK = Pixel(430, 105)

# TODO: FIX TITAN SNIPE
ABILITY_ANCHOR_PIXEL = Pixel(321, 113)
ABILITY_OFFSETX = 106
ABILITY_OFFSETY = 37

# ROW 1 ABILITIES
ABILITY_STRONG_ATTACK = Pixel(531, 113)
ABILITY_PARRY = Pixel(636, 113)
ABILITY_PIERCING_ATTACK = Pixel(741, 113)
ABILITY_ULTIMATE_ATTACK = Pixel(846, 113)
ABILITY_ROW1_READY_COLOR = "F89B9B"
# ROW 2 ABILITIES
ABILITY_BLOCK = Pixel(321, 150)
ABILITY_DEFENSIVE_BUFF = Pixel(426, 150)
ABILITY_HEAL = Pixel(531, 150)
ABILITY_OFFENSIVE_BUFF = Pixel(636, 150)
ABILITY_CHARGE = Pixel(741, 150)
ABILITY_ULTIMATE_BUFF = Pixel(846, 150)
ABILITY_ROW2_READY_COLOR = "F89B9B"
# ROW 3 ABILITIES
ABILITY_PARALYZE_GAZE = Pixel(321, 186)
ABILITY_HYPER_REGEN = Pixel(426, 186)
ABILITY_BEAST_MODE = Pixel(531, 186)
ABILITY_ROW3_READY_COLOR = "C39494"

# TODO: FIX ABILITY NUMBERING TO NEW SCHEME
ABILITY_PRIORITY = {1: 6,  # Strong
                    2: 8,  # Parry
                    3: 9,  # Piercing
                    4: 10,  # Ultimate
                    5: 4,  # Block
                    6: 5,  # Defensive
                    9: 12  # Charge
                    }  # Paralyze

# titan dictionaries
TITAN_PT = {"GRB": {"p": 1.3e3, "t": 1.3e3}, "GCT": {"p": 5e3, "t": 4e3},
            "jake": {"p": 1.4e4, "t": 1.2e4}, "UUG": {"p": 4e5, "t": 3e5},
            "walderp": {"p": 5.5e6, "t": 3.75e6},
            "BEAST1": {"p": 6e8, "t": 6e8}, "BEAST2": {"p": 6e9, "t": 6e9},
            "BEAST3": {"p": 6e10, "t": 6e10}, "BEAST4": {"p": 6e11, "t": 6e11}}

TITAN_ZONE = {"GRB": 7, "GCT": 9, "jake": 12, "UUG": 15, "walderp": 17,
              "BEAST1": 20, "BEAST2": 20, "BEAST3": 20, "BEAST4": 20}

OCR_ADV_POW = OCRBox(370, 296, 483, 313)
OCR_ADV_TOUGH = OCRBox(406, 313, 506, 330)
OCR_ADV_TITAN = OCRBox(560, 277, 685, 330)
OCR_ADV_ENEMY_CHECK = OCRBox(766, 382, 889, 403)
OCR_COMBAT_LOG = OCRBox(310, 496, 600, 589)

# MENU OFFSETS

MENU_OFFSET_X = 230
MENU_FIGHT = Pixel(MENU_OFFSET_X, 75)
MENU_PIT = Pixel(MENU_OFFSET_X, 105)
MENU_ADVENTURE = Pixel(MENU_OFFSET_X, 135)
MENU_INVENTORY = Pixel(MENU_OFFSET_X, 165)
MENU_AUGMENTATIONS = Pixel(MENU_OFFSET_X, 195)
MENU_ADV_TRAINING = Pixel(MENU_OFFSET_X, 225)
MENU_TIME_MACHINE = Pixel(MENU_OFFSET_X, 255)
MENU_BLOOD_MAGIC = Pixel(MENU_OFFSET_X, 285)
MENU_WANDOOS = Pixel(MENU_OFFSET_X, 315)
MENU_NGU = Pixel(MENU_OFFSET_X, 345)
MENU_YGGDRASIL = Pixel(MENU_OFFSET_X, 375)
MENU_DIGGERS = Pixel(MENU_OFFSET_X, 405)
MENU_BEARD = Pixel(MENU_OFFSET_X, 435)
MENU_QUESTING = Pixel(MENU_OFFSET_X, 465)
MENU_HACKS = Pixel(MENU_OFFSET_X, 495)
MENU_WISHES = Pixel(MENU_OFFSET_X, 525)
MENU_ITEMS = {
    'fight': MENU_FIGHT, 'pit': MENU_PIT, 'adventure': MENU_ADVENTURE,
    'inventory': MENU_INVENTORY, 'augmentations': MENU_AUGMENTATIONS,
    'advtraining': MENU_ADV_TRAINING, 'timemachine': MENU_TIME_MACHINE,
    'bloodmagic': MENU_BLOOD_MAGIC, 'wandoos': MENU_WANDOOS, 'ngu': MENU_NGU,
    'yggdrasil': MENU_YGGDRASIL, 'digger': MENU_DIGGERS, 'beard': MENU_BEARD,
    'questing': MENU_QUESTING, 'hacks': MENU_HACKS, 'wishes': MENU_WISHES,
}
NUMBER_INPUT_BOX = Pixel(440, 20)
EXP = Pixel(90, 450)
SAVE = Pixel(23, 483)

# SETTINGS
GAME_SETTINGS = Pixel(30, 542)
SETTINGS_PAGE_1 = Pixel(365, 80)
SETTINGS_PAGE_2 = Pixel(425, 80)
TO_SCIENTIFIC = Pixel(385, 170)
CHECK_FOR_UPDATE_OFF = Pixel(420, 400)
FANCY_TITAN_HP_BAR_OFF = Pixel(585, 410)
DISABLE_HIGHSCORE = Pixel(900, 410)
SIMPLE_INVENTORY_SHORTCUT_ON = Pixel(350, 420)

# FIGHT BOSS OFFSETS

NUKE = Pixel(620, 145)
FIGHT = Pixel(620, 275)
FIGHT_STOP = Pixel(625, 165)

# INVENTORY OFFSETS
EQUIPMENT_SLOTS = {"accessory1": Pixel(480, 65),
                   "accessory2": Pixel(480, 115),
                   "accessory3": Pixel(480, 165),
                   "accessory4": Pixel(480, 215),
                   "accessory5": Pixel(425, 210),
                   "accessory6": Pixel(425, 160),
                   "head": Pixel(525, 65),
                   "chest": Pixel(525, 115),
                   "legs": Pixel(525, 165),
                   "boots": Pixel(525, 210),
                   "weapon": Pixel(575, 115),
                   "cube": Pixel(625, 115)}
LOADOUT_Y = 255
LOADOUT = {1: Pixel(330, LOADOUT_Y), 2: Pixel(360, LOADOUT_Y), 3: Pixel(390, LOADOUT_Y), 4: Pixel(420, LOADOUT_Y),
           5: Pixel(450, LOADOUT_Y),
           6: Pixel(480, LOADOUT_Y), 7: Pixel(510, LOADOUT_Y), 8: Pixel(540, LOADOUT_Y), 9: Pixel(570, LOADOUT_Y),
           10: Pixel(600, LOADOUT_Y)}

INVENTORY_SLOTS = Pixel(300, 330)
INVENTORY_AREA = OCRBox(315, 290, 930, 560)
INVENTORY_PAGE_Y = 574
INVENTORY_PAGE = [Pixel(364, INVENTORY_PAGE_Y), Pixel(428, INVENTORY_PAGE_Y), Pixel(492, INVENTORY_PAGE_Y),
                  Pixel(560, INVENTORY_PAGE_Y), Pixel(620, INVENTORY_PAGE_Y)]
# TIME MACHINE OFFSETS
TM_SPEED = Pixel(532, 233)
TM_MULT = Pixel(532, 330)
TM_SPEED_MINUS = Pixel(570, 236)
TM_MULT_MINUS = Pixel(570, 335)
OCR_TM_MAGIC_ALLOCATED = OCRBox(690, 324, 847, 341)
OCR_TM_ENERGY_ALLOCATED = OCRBox(690, 224, 847, 241)
OCR_TM_ENERGY_LVL = OCRBox(849, 223, 935, 246)
OCR_TM_MAGIC_LVL = OCRBox(843, 321, 946, 343)

# BLOOD MAGIC OFFSETS
BM_LOCKED = Pixel(231, 276)

BM_X = 570
BM = {0: Pixel(BM_X, 228), 1: Pixel(BM_X, 263), 2: Pixel(BM_X, 298), 3: Pixel(BM_X, 333),
      4: Pixel(BM_X, 369), 5: Pixel(BM_X, 403), 6: Pixel(BM_X, 438), 7: Pixel(BM_X, 473)}

BM_SPELL = Pixel(390, 115)
BM_PILL = Pixel(744, 216)
BM_GUFFIN_A = Pixel(395, 435)
BM_GUFFIN_B = Pixel(735, 435)
BM_NUMBER = Pixel(400, 220)
BM_AUTO_NUMBER = Pixel(512, 219)
BM_AUTO_GOLD = Pixel(849, 311)
BM_AUTO_DROP = Pixel(511, 311)

BM_RECLAIM_X = 530
BM_RECLAIM = [Pixel(BM_RECLAIM_X, 228), Pixel(BM_RECLAIM_X, 263), Pixel(BM_RECLAIM_X, 298), Pixel(BM_RECLAIM_X, 333),
              Pixel(BM_RECLAIM_X, 369), Pixel(BM_RECLAIM_X, 403), Pixel(BM_RECLAIM_X, 438), Pixel(BM_RECLAIM_X, 473)]

OCR_BM_SPELL_TEXT = OCRBox(440, 350, 800, 412)
OCR_BM_ALLOCATED = [OCRBox(670, 219, 827, 236),  # Poke yourself with a tack
                    OCRBox(670, 254, 827, 271),  # Fifty Papercuts
                    OCRBox(670, 289, 827, 306),  # A Big-Ass Hickey
                    OCRBox(670, 324, 827, 341),  # Eat a bowl of barbed wire
                    OCRBox(670, 359, 827, 376),  # Grand Theft Blood Bank
                    OCRBox(670, 394, 827, 411),  # Self Decapitation
                    OCRBox(670, 429, 827, 446),  # Hug a Woodchipper
                    OCRBox(670, 464, 827, 481)]  # Turn Yourself inside out

# TODO: AUGMENTATION OFFSETS
AUGMENT_X = 535

AUGMENT = {"SS": Pixel(AUGMENT_X, 263), "DS": Pixel(AUGMENT_X, 292), "MI": Pixel(AUGMENT_X, 329),
           "DTMT": Pixel(AUGMENT_X, 357), "CI": Pixel(AUGMENT_X, 394), "ML": Pixel(AUGMENT_X, 422),
           "SM": Pixel(AUGMENT_X, 459), "AA": Pixel(AUGMENT_X, 487), "EB": Pixel(AUGMENT_X, 525),
           "CS": Pixel(AUGMENT_X, 552), "AE": Pixel(AUGMENT_X, 450), "ES": Pixel(AUGMENT_X, 478),
           "LS": Pixel(AUGMENT_X, 516), "QSL": Pixel(AUGMENT_X, 544)}

AUG_MINUS_X = 575

AUG_SCROLL_TOP = Pixel(945, 264)
AUG_SCROLL_BOT = Pixel(945, 575)
AUG_SCROLL_SANITY_TOP = Pixel(943, 261)
AUG_SCROLL_SANITY_BOT = Pixel(943, 578)
AUG = {"LEVELS": [OCRBox(694, 250, 816, 276),
                  OCRBox(694, 283, 816, 300),
                  OCRBox(694, 317, 816, 339),
                  OCRBox(694, 347, 816, 369),
                  OCRBox(694, 382, 816, 404),
                  OCRBox(694, 412, 816, 434),
                  OCRBox(694, 447, 816, 469),
                  OCRBox(694, 477, 816, 499),
                  OCRBox(694, 512, 816, 534),
                  OCRBox(694, 542, 816, 564)],

       "Energy": [OCRBox(818, 250, 940, 276),
                  OCRBox(818, 283, 940, 300),
                  OCRBox(818, 317, 940, 339),
                  OCRBox(818, 347, 940, 369),
                  OCRBox(818, 382, 940, 404),
                  OCRBox(818, 412, 940, 434),
                  OCRBox(818, 447, 940, 469),
                  OCRBox(818, 477, 940, 499),
                  OCRBox(818, 512, 940, 534),
                  OCRBox(818, 542, 940, 564)]}

# TODO: NGU OFFSETS
NGU_TARGET = Pixel(635, 205)
NGU_MAGIC = Pixel(380, 120)
NGU_MINUS = Pixel(551, 207)
NGU_PLUS = Pixel(517, 207)
NGU_CAP = Pixel(590, 207)
NGU_CAP_ALL = Pixel(625, 160)
NGU_OVERCAP = Pixel(430, 135)
NGU_EVIL = ColorPixel(778, 146, "323232")

NGU_BAR_MIN = Pixel(306, 215)
NGU_BAR_MAX = Pixel(503, 215)
NGU_BAR_OFFSET_Y = 35

# TODO: Make into dict ADVTRAINING
ADV_TRAINING_TOUGHNESS = Pixel(890, 230)
ADV_TRAINING_POWER = Pixel(890, 270)
ADV_TRAINING_BLOCK = Pixel(890, 310)
ADV_TRAINING_WANDOOS_ENERGY = Pixel(890, 350)
ADV_TRAINING_WANDOOS_MAGIC = Pixel(890, 390)
OCR_ADV_TR_0_ALLOCATED = OCRBox(648, 215, 775, 238)
OCR_ADV_TR_0_LVL = OCRBox(523, 215, 656, 238)

OCR_ADV_TR_1_ALLOCATED = OCRBox(648, 255, 775, 278)
OCR_ADV_TR_1_LVL = OCRBox(523, 255, 656, 278)

OCR_ADV_TR_2_ALLOCATED = OCRBox(648, 295, 775, 318)
OCR_ADV_TR_2_LVL = OCRBox(523, 295, 656, 318)

OCR_ADV_TR_3_ALLOCATED = OCRBox(648, 335, 775, 358)
OCR_ADV_TR_3_LVL = OCRBox(523, 334, 656, 357)

OCR_ADV_TR_4_ALLOCATED = OCRBox(648, 375, 775, 398)
OCR_ADV_TR_4_LVL = OCRBox(523, 374, 656, 397)

# YGGDRASIL OFFSETS
HARVEST = Pixel(814, 450)
FRUIT_GOLD = Pixel(350, 180)
FRUIT_POWER_A = Pixel(560, 180)
FRUIT_ADV = Pixel(775, 180)
FRUIT_KNOWLEDGE = Pixel(350, 270)
FRUIT_POM = Pixel(560, 270)
FRUIT_LUCK = Pixel(775, 270)
FRUIT_POWER_B = Pixel(350, 370)
FRUIT_ARB = Pixel(560, 370)
FRUIT_NUMBERS = Pixel(775, 370)
FRUITS = {
    1: FRUIT_GOLD,
    2: FRUIT_POWER_A,
    3: FRUIT_ADV,
    4: FRUIT_KNOWLEDGE,
    5: FRUIT_POM,
    6: FRUIT_LUCK,
    7: FRUIT_POWER_B,
    8: FRUIT_ARB,
    9: FRUIT_NUMBERS
}
YGG_PAGE1 = Pixel(340, 112)
YGG_PAGE2 = Pixel(405, 112)
YGG_ACTION_SEARCH_AREA = OCRBox(317, 163, 806, 382)
YGG_EAT_ALL = Pixel(815, 490)
YGG_EAT_MAX_TIER = Pixel(815, 445)
YGG_ACTIVATE = [OCRBox(323, 168, 374, 185),  # Fruit of Gold/Rage
                OCRBox(534, 168, 585, 185),  # Fruit of Power Alpha/MacGuffin alpha
                OCRBox(746, 168, 797, 185),  # Fruit of Adventure/Power Delta?
                OCRBox(324, 264, 375, 281),  # Fruit of Knowledge/Watermellon
                OCRBox(535, 264, 586, 281),  # Pomegranate/MacGuffin Beta
                OCRBox(746, 264, 797, 281),  # Fruit of Luck/NA
                OCRBox(323, 359, 374, 376),  # Fruit of Power Beta/NA
                OCRBox(534, 359, 585, 376),  # Fruit of Arbitrariness/NA
                OCRBox(746, 359, 797, 376)]  # Fruit of numbers/NA

# REBIRTH OFFSETS
REBIRTH = Pixel(90, 420)
REBIRTH_BUTTON = Pixel(545, 520)
CONFIRM = Pixel(425, 320)
CHALLENGE_BUTTON = Pixel(700, 520)
CHALLENGE = Pixel(380, 152)
CHALLENGEOFFSET = 30
OCR_REBIRTH_TIME = OCRBox(35, 375, 140, 392)

# PIT OFFSETS
PIT_CHECK = Pixel(195, 108)
PIT = Pixel(630, 290)
PIT_CONFIRM = Pixel(437, 317)
SPIN_MENU = Pixel(820, 235)
SPIN = Pixel(713, 562)

# WANDOOS
WANDOOS_ENERGY = Pixel(626, 252)
WANDOOS_MAGIC = Pixel(626, 350)
WANDOOS_VERSION = [Pixel(325, 420), Pixel(325, 445), Pixel(325, 470)]
OCR_WANDOOS_MAGIC_ALLOCATED = OCRBox(646, 339, 803, 356)
OCR_WANDOOS_ENERGY_ALLOCATED = OCRBox(646, 241, 803, 258)

# OCR OFFSETS
OCR_CNGU = OCRBox(381, 150, 569, 174)
OCR_NNGU = OCRBox(681, 150, 869, 174)
OCR_BOSS = OCRBox(765, 308, 890, 323)
OCR_PP = OCRBox(785, 25, 901, 43)
OCR_EXP = OCRBox(340, 70, 900, 95)  # From EXP Menu
OCR_POW = OCRBox(469, 295, 619, 311)
OCR_CAP = OCRBox(629, 295, 779, 311)
OCR_BAR = OCRBox(790, 295, 939, 311)
OCR_ECAP = OCRBox(9, 44, 165, 63)
OCR_TOTAL_EXP = OCRBox(510, 365, 928, 400)  # From MISC Info
OCR_NGU_E = OCRBox(820, 190, 940, 219)

# STATS OCR
OCR_ENERGY = OCRBox(13, 31, 161, 53)
OCR_MAGIC = OCRBox(13, 71, 161, 91)
OCR_R3 = OCRBox(12, 110, 162, 133)

# OCR CHALLENGES
OCR_CHALLENGE_NAME = OCRBox(465, 87, 750, 104)
OCR_CHALLENGE_24HC_TARGET = OCRBox(479, 267, 771, 297)

# BEARD OFFSETS

BEARD_X = {1: 312, 2: 338, 3: 312, 4: 1}

# TODO: DIGGER OFFSETS
DIG_PAGE_Y = 110
DIG_PAGE = [Pixel(340, DIG_PAGE_Y), Pixel(405, DIG_PAGE_Y), Pixel(470, DIG_PAGE_Y)]

DIG_ACTIVE = {1: Pixel(341, 237), 2: Pixel(658, 237), 3: Pixel(341, 427), 4: Pixel(658, 427)}
DIG_CAP = {1: Pixel(550, 185), 2: Pixel(865, 185), 3: Pixel(550, 375), 4: Pixel(865, 375)}

DIG_LEVEL = [Pixel(535, 235), Pixel(850, 235), Pixel(535, 420), Pixel(850, 420)]

DIG_DEACTIVATE_ALL = Pixel(906, 97)

# QUESTING OFFSETS

QUESTING_START_QUEST = Pixel(700, 165)
QUESTING_SKIP_QUEST = Pixel(855, 165)
QUESTING_SUBCONTRACT = Pixel(470, 560)
QUESTING_QUEST_COMPLETE = "this quest can be handed in"
QUESTING_NO_QUEST_ACTIVE = "start quest"
QUESTING_MINOR_QUEST = "this is a minor quest"
QUESTING_USE_MAJOR = Pixel(694, 207)
QUESTING_BUTTER = Pixel(825, 245)

OCR_QUESTING_QP = OCRBox(500, 60, 683, 84)
OCR_QUESTING_LEFT_TEXT = OCRBox(301, 296, 617, 497)
OCR_QUESTING_MAJORS = OCRBox(790, 300, 857, 317)
QUESTING_ZONES = ["safe zone", "tutorial zone", "sewers", "forest", "cave of many things", "the sky",
                  "high\nsecurity base", "grb", "clock dimension", "gct", "2d universe", "ancient battlefield",
                  "jfa", "a very\nstrange place", "mega\nlands", "uug", "the beardverse", "waldo", "badly drawn world",
                  "boring-ass earth", "thebeasto", "chocolate world", "the evilverse", "pretty pink princess",
                  "greasynerdman", "meta land",
                  "interdimensional party", "thegodmom"]

QUESTING_FILENAMES = ["q1.png", "q2.png", "q3.png", "q4.png", "q5.png", "q6.png", "q7.png", "q8.png", "q9.png",
                      "q10.png"]

# SELLOUT

SELLOUT = Pixel(235, 550)
SELLOUT_BOOST_2 = Pixel(520, 147)
SELLOUT_MUFFIN_USE = Pixel(768, 256)
SELLOUT_MUFFIN_BUY = Pixel(860, 255)
OCR_MUFFIN = OCRBox(785, 204, 936, 240)
OCR_AP = OCRBox(450, 73, 800, 100)

# EXP COSTS PER UNIT
EPOWER_COST = 150
ECAP_COST = 0.004
EBAR_COST = 80
MPOWER_COST = 450
MCAP_COST = 0.012
MBAR_COST = 240

APOWER_COST = 3
ATOUGHNESS_COST = 3
AHEALTH_COST = 0.3
AREGEN_COST = 50

HPOWER_COST = 15000000
HCAP_COST = 400
HBAR_COST = 8000000

RATTACK_COST = 3
RDEFENSE_COST = 3

# EXP MENU
XP_MENU = Pixel(90, 450)
MAGIC_MENU = Pixel(470, 110)
ADVENTURE_MENU = Pixel(570, 110)
RICH_MENU = Pixel(785, 110)
EXP_HACK_MENU = Pixel(420, 140)

EM_POW_BOX = Pixel(537, 522)
EM_CAP_BOX = Pixel(707, 522)
EM_BAR_BOX = Pixel(862, 522)
EM_ADV_BOX = Pixel(367, 522)

EM_POW_BUY = Pixel(542, 557)
EM_CAP_BUY = Pixel(703, 557)
EM_BAR_BUY = Pixel(864, 557)
EM_ADV_BUT = Pixel(367, 577)

EM_RICHA_BOX = Pixel(700, 450)
EM_RICHD_BOX = Pixel(860, 450)

EM_RICHA_BUY = Pixel(700, 490)
EM_RICHD_BUY = Pixel(860, 490)

# INFO
INFO = Pixel(100, 542)
MISC = Pixel(355, 200)
STAT_BREAKDOWN = Pixel(875, 35)

# STAT BREAKDOWNS

BREAKDOWN_ATT_DEF = Pixel(355, 85)
BREAKDOWN_E = Pixel(470, 85)
BREAKDOWN_M = Pixel(580, 85)
BREAKDOWN_R = Pixel(690, 85)
BREAKDOWN_AUGS = Pixel(800, 85)
BREAKDOWN_NGU = Pixel(900, 85)

BREAKDOWN_EXP = Pixel(355, 115)
BREAKDOWN_MISC = Pixel(470, 115)
BREAKDOWN_ADV = Pixel(580, 115)
BREAKDOWN_MISC_ADV = Pixel(690, 115)
BREAKDOWN_BEARDS = Pixel(800, 115)
BREAKDOWN_WANDOOS = Pixel(900, 115)

OCR_BREAKDOWN_E = OCRBox(331, 160, 935, 574)
BREAKDOWN_ECAP = OCRBox(630, 522, 888, 540)

BREAKDOWN_MPOW = OCRBox(634, 266, 760, 284)
BREAKDOWN_MCAP = OCRBox(630, 522, 888, 540)
BREAKDOWN_MISC_SCROLL_DRAG_START = Pixel(956, 132)
BREAKDOWN_MISC_SCROLL_DRAG_END = Pixel(956, 150)

# PIXEL CHECKS
# TODO: CONVERT to ColorPixel of COLOR_
IS_BOSS_CROWN = ColorPixel(715, 277, 'F7EF29')
IS_ENEMY_ALIVE = ColorPixel(*HEALTH, ['D93030', 'EB3434', 'DB3131',
                                      'DA3030'])  # If you reduce the enemy healthbar to 1px, the color changes for some reason
IS_DEAD = ColorPixel(*HEALTH, ['EBEBEB', 'ECECEC'])
IS_ITOPOD_ACTIVE = ColorPixel(594, 277, '000000')  # Checks color of pixel in "Floor x" text
IS_IDLE = ColorPixel(416, 86, 'FFEB04')  # top right yellow pixel
IS_SAVE_READY = ColorPixel(*SAVE, '99FF99')
IS_PIT_READY = ColorPixel(*PIT_CHECK, '7FD23B')
IS_SPIN_READY = ColorPixel(*PIT_CHECK, 'FFD23B')
COLOR_CHALLENGE_ACTIVE = ColorPixel(391, 111, '000000')
COLOR_TM_LOCKED = ColorPixel(188, 257, '96A7B7')
COLOR_BM_LOCKED = ColorPixel(*BM_LOCKED, ['96A7B7', '7B4A94'])
COLOR_BM_LOCKED_ALT = ColorPixel(*BM_LOCKED, '7B4A94')
COLOR_SPELL_READY = ColorPixel(*BM_LOCKED, 'BA13A7')
PLAYER_HEAL_THRESHOLD = ColorPixel(500, 410, 'FFFFFF')
QUESTING_IDLE_INACTIVE = ColorPixel(386, 555, '111111')  # Pixel in the subcontracting button
COLOR_BM_AUTO_NUMBER = ColorPixel(*BM_AUTO_NUMBER, '000000')
COLOR_BM_AUTO_DROP = ColorPixel(*BM_AUTO_DROP, '000000')
COLOR_BM_AUTO_GOLD = ColorPixel(*BM_AUTO_GOLD, '000000')
COLOR_QUESTING_USE_MAJOR = ColorPixel(*QUESTING_USE_MAJOR, '000000')
COLOR_WANDOOS_ENERGY_BB = ColorPixel(526, 250, ['58CC7E', '59CF81'])
COLOR_WANDOOS_MAGIC_BB = ColorPixel(526, 350, ['718DF1', '738FF5'])
COLOR_ADV_TRAINING_LOCKED = ColorPixel(195, 225, '96A7B7')

HACKS = {1: Pixel(570, 230), 2: Pixel(890, 230),
         3: Pixel(570, 320), 4: Pixel(890, 320),
         5: Pixel(570, 415), 6: Pixel(890, 415),
         7: Pixel(570, 510), 8: Pixel(890, 510)}

HACK_PAGE_Y = 182
HACK_PAGE = [Pixel(335, HACK_PAGE_Y), Pixel(395, HACK_PAGE_Y)]

# WISHES
COLOR_WISH_COMPLETED = 'FFF200'
COLOR_WISH_STARTED = '244A63'
COLOR_WISH_NEW = '122532'
COLOR_WISH_ACTIVE = '3EBEBE'
COLOR_WISH_INACTIVE = 'B20000'
WISH_BORDER = Pixel(307, 323)
WISH_PAGE_Y = 255
WISH_PAGE = [Pixel(340, WISH_PAGE_Y), Pixel(405, WISH_PAGE_Y), Pixel(470, WISH_PAGE_Y), Pixel(535, WISH_PAGE_Y)]
WISH_SELECTION = Pixel(313, 278)
WISH_SELECTION_OFFSET = Pixel(92, 106)
WISH_CLEAR_WISH = Pixel(800, 112)
WISH_E_ADD = Pixel(590, 220)
WISH_M_ADD = Pixel(720, 220)
WISH_R_ADD = Pixel(860, 220)
OCR_WISH_SLOTS = OCRBox(708, 120, 755, 135)
