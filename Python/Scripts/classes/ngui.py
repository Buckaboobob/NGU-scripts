import pygame
from classes.inputs import Inputs
import coordinates as coords
from classes.navigation import Navigation

pygame.init()


class NGUI(Navigation, Inputs):
    allocated = {"TM": [0, 0],
                 "Wandoos": [0, 0],
                 "Augment": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 "AUG_TOTAL": 0,
                 "BM": [0, 0, 0, 0, 0, 0, 0, 0]}

    def get_tm_allocated(self):
        self.menu('timemachine')
        bmp = self.get_bitmap()
        self.allocated['TM'][0] = self.get_ocr_number(*coords.OCR_TM_ENERGY_ALLOCATED, bmp=bmp)
        self.allocated['TM'][1] = self.get_ocr_number(*coords.OCR_TM_MAGIC_ALLOCATED, bmp=bmp)
        return

    def get_wandoos_allocated(self):
        self.menu("wandoos")
        bmp = self.get_bitmap()
        self.allocated['Wandoos'][0] = self.get_ocr_number(*coords.OCR_WANDOOS_ENERGY_ALLOCATED, bmp)
        self.allocated['Wandoos'][1] = self.get_ocr_number(*coords.OCR_WANDOOS_MAGIC_ALLOCATED, bmp)
        return

    def get_aug_allocated(self):
        self.menu("augmentations")
        bmp = self.get_bitmap()
        b = 0
        for a in range(0, 10, 1):
            self.allocated['Augment'][a] = self.get_ocr_number(*coords.AUG["Energy"][a], bmp=bmp)
            b += self.allocated['Augment'][a]
#            print("{}: {}".format(a, self.allocated["Augment"][a]))
        self.allocated['Aug_Total'] = b
        print("Aug Total Energy: {}".format(str(b)))
        return
