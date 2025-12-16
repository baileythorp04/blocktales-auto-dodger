import time
import pyautogui
from constants import *
from helpers import *

class Dodged_State():
    start_time = 0
    waiting_to_check_walking = False
    enemy_is_walking = False
    current_enemy_place = 3 #TODO make this track enemy attacks


    next_triple_no = 0
    finished_dodging = True
    finished_barrel = True



    def enable(self):
        self.start_time = time.time()
        self.enemy_is_walking = False
        self.waiting_to_check_walking = True

        self.next_triple_no = 0
        self.finished_barrel = False
        self.finished_dodging = False
        


    def disable(self):
        self.finished_dodging = True


    def try_dodge(self):
        if (not self.finished_dodging):
            if (self.enemy_is_walking):

                if (not self.finished_barrel):
                    barrel_dodge_time = BARREL_TIMING + WALK_DELAY_4 + SAFETY_OFFSET
                    if (time_has_passed(self.start_time, barrel_dodge_time)):
                        self.do_dodge("barrel", barrel_dodge_time)
                        self.finished_barrel = True #after dodging barrel, dont do it again

                single_dodge_time = SINGLE_TIMING + WALK_DELAY_4 + SAFETY_OFFSET
                if (time_has_passed(self.start_time, single_dodge_time)):
                    self.do_dodge("single", single_dodge_time)
                    self.finished_dodging = True #after dodging single, stop dodging

            else: #not dodging walking
            
                triple_dodge_time = TRIPLE_TIMINGS[self.next_triple_no] + SAFETY_OFFSET
                if (time_has_passed(self.start_time, triple_dodge_time)):
                    self.do_dodge(f"triple {self.next_triple_no}", triple_dodge_time)
                    self.next_triple_no += 1
                    if (self.next_triple_no == 3):
                        self.finished_dodging = True #after dodging all three, stop dodging
    
    def check_walk(self, frame):
        if (self.waiting_to_check_walking):
            if (time_has_passed(self.start_time, ENEMY_MOVE_TIME)):
                self.waiting_to_check_walking = False
                color = get_pixel(frame, *HEALTH_POSES[self.current_enemy_place])
                if (color == HEALTH_RED or color == HEALTH_YELLOW):
                    print("enemy not walking")
                else:
                    self.enemy_is_walking = True
                    print("detected enemy walking")

        #TODO it may be a bad idea to scan pixels mid-loop, but its only once per dot so i think its ok


    def do_dodge(self, name, expected_time):
        print(f"dodge {name} preclick: {(time.time()-self.start_time)/0.03333}")
        print(f"expected: {expected_time}")
        pyautogui.leftClick()
        pyautogui.press("ctrl")

