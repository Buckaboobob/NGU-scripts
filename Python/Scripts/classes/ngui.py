import pygame
from classes.inputs import Inputs
import coordinates as coords
from classes.navigation import Navigation

pygame.init()


class NGUI(Navigation, Inputs):
    allocated = {"TM": [0, 0],
                 "Wandoos": [0, 0],
                 "Augment": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 "BM": [0, 0, 0, 0, 0, 0, 0, 0]}

    def get_tm_allocated(self):
        self.menu('timemachine')
        bmp = self.get_bitmap()
        self.allocated['TM'][0] = self.get_ocr_number(*coords.OCR_TM_ENERGY_ALLOCATED, bmp=bmp, debug=True)
        self.allocated['TM'][1] = self.get_ocr_number(*coords.OCR_TM_MAGIC_ALLOCATED, bmp=bmp, debug=True)
        return

    def get_wandoos_allocated(self):
        self.menu("wandoos")
        bmp = self.get_bitmap()
        self.allocated['Wandoos'][0] = self.get_ocr_number(*coords.OCR_WANDOOS_ENERGY_ALLOCATED, bmp)
        self.allocated['Wandoos'][1] = self.get_ocr_number(*coords.OCR_WANDOOS_MAGIC_ALLOCATED, bmp)
        return
