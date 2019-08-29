import pygame
from classes.inputs import Inputs
import coordinates as coords
from classes.navigation import Navigation as navigation

pygame.init()


class NGUI:
    def __init__(self, nav_obj, input_obj):
        NGUI.nav = nav_obj
        NGUI.i = input_obj

    allocated = {"TM": [0, 0],
                 "Wandoos": [0, 0],
                 "Augment": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 "BM": [0, 0, 0, 0, 0, 0, 0, 0]}

    def get_tm_allocated(self):
        self.nav.menu("timemachine")
        self.allocated['TM'][0] = self.i.get_ocr_number(*coords.OCR_TM_ENERGY_ALLOCATED)
        self.allocated['TM'][1] = self.i.get_ocr_number(*coords.OCR_TM_MAGIC_ALLOCATED)
        return

    def get_wandoos_allocated(self):
        navigation.menu(self.nav, "wandoos")
        self.allocated['Wandoos'][0] = Inputs.get_ocr_number(*coords.OCR_WANDOOS_ENERGY_ALLOCATED)
        self.allocated['Wandoos'][1] = Inputs.get_ocr_number(*coords.OCR_WANDOOS_MAGIC_ALLOCATED)
        return
