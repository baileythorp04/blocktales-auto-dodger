import mss
from constants import *

class Dots:
    dots = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
    line = LOG_BACKGROUND
    has_4_dots = False

    def reset(self):
        self.dots = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]
        self.line = LOG_BACKGROUND
        self.has_4_dots = False


    def check_for_dot_change(self, img: mss):
        #if the log is not full with 4 lines, check each one to see if it turned gray
        if (not self.has_4_dots):
            for i in range(4):
                new_color = img.pixel(*LOG_DOT_POSES[i])
                if (self.dots[i] != new_color): #update each dot to the newest color
                    self.dots[i] = new_color

                    if (new_color == LOG_GRAY):
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
            new_dot_color = img.pixel(*LOG_DOT_POSES[3])
            old_dot_color = self.dots[3]
            self.dots[3] = new_dot_color

            new_line_color = img.pixel(*LOG_LINECHECK_POS)
            old_line_color = self.line
            self.line = new_line_color

            #if dot is gray AND:
            #dot had just changed to gray OR line had just turned into background (line disappeared)
            if (new_dot_color == LOG_GRAY and ((old_dot_color != LOG_GRAY) or (old_line_color != LOG_BACKGROUND and new_line_color == LOG_BACKGROUND))):
                print("dot found")
                return True