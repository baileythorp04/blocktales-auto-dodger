import time
import pyautogui
from constants import *
from helpers import time_has_passed

class Dodged_State():
    start_time = 0
    finished_dodging = True
    finished_barrel = True


    def enable(self):
        self.start_time = time.time()
        self.finished_barrel = False
        self.finished_dodging = False
        #set dodging_walking



    def disable(self):
        self.finished_dodging = True


    def do_dodge(self):
        if (not self.finished_dodging):

            if (not self.finished_barrel):
                barrel_dodge_time = BARREL_TIMING + DELAY_4 + SAFETY_OFFSET + DOT_DELAY_OFFSET
                if (time_has_passed(self.start_time, barrel_dodge_time)):
                    dodged_barrel = True
                    print(f"dodge barrel preclick: {(time.time()-self.start_time)/0.03333}")
                    print(f"expected: {barrel_dodge_time}")
                    pyautogui.leftClick()
                    pyautogui.press("ctrl")

                    self.finished_barrel = True #after dodging barrel, dont do it again

            single_dodge_time = SINGLE_TIMING + DELAY_4 + SAFETY_OFFSET + DOT_DELAY_OFFSET
            if (time_has_passed(self.start_time, single_dodge_time)):
                dodged_single = True
                print(f"dodge single preclick: {(time.time()-self.start_time)/0.03333}")
                print(f"expected: {single_dodge_time}")
                pyautogui.leftClick()
                pyautogui.press("ctrl")


                self.finished_dodging = True #after dodging single, stop dodging
