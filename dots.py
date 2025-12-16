from constants import *
from helpers import *
import pyautogui

class Dots:
    new_dots = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
    old_dots = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
    new_line = LOG_BACKGROUND
    old_line = LOG_BACKGROUND
    has_4_dots = False

    def reset(self):
        self.new_dots = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
        self.old_dots = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
        self.new_line = LOG_BACKGROUND
        self.old_line = LOG_BACKGROUND
        self.has_4_dots = False

    def scan_dots(self, frame):
        for i in range(4):
            self.new_dots[i] = get_pixel(frame, *LOG_DOT_POSES[i])
        self.new_line = get_pixel(frame, *LOG_LINECHECK_POS)

    def check_for_dot_change(self):
        res = self.cfdc_logic()
        self.old_dots = self.new_dots
        self.old_line = self.new_line
        return res

    def cfdc_logic(self):
        #if the log is not full with 4 lines, check each one to see if it turned gray
        if (not self.has_4_dots):
            for i in range(4):
                if (self.old_dots[i] != self.new_dots[i]): #update each dot to the newest color

                    if (self.new_dots[i] == LOG_GRAY):
                        if (i == 3):
                            self.has_4_dots = True

                        if (i == 0):
                            print("player's dot found")
                            return False
                        else:
                            print("dot found")
                            return True
        #else, only check the last dot
        else:

            #if dot is gray AND:
            #dot had just changed to gray OR line had just turned into background (line disappeared)
            if (self.new_dots[3] == LOG_GRAY and ((self.old_dots[3] != LOG_GRAY) or (self.old_line != LOG_BACKGROUND and self.new_line == LOG_BACKGROUND))):
                print("dot found")
                return True