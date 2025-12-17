import time
import pyautogui
from battlefield import Battlefield
from constants import *
from helpers import *

class Dodged_State():
    start_time = 0
    field = Battlefield()


    in_place_health_bars = [True, True, True, True]
    waiting_to_check_walking = False
    active_enemy_position = -1
    active_enemy_is_walking = False

    next_triple_no = 0
    finished_dodging = True
    finished_barrel = True

    

    def enable(self):
        self.start_time = time.time()

        self.in_place_health_bars = [True, True, True, True]
        self.waiting_to_check_walking = True
        self.active_enemy_position = self.field.get_next_enemy_position()
        self.active_enemy_is_walking = False

        self.next_triple_no = 0
        self.finished_barrel = False
        self.finished_dodging = False

    def disable(self):
        self.finished_dodging = True
        self.field.reset_attacks()

    def do_dodge(self, name, expected_time):
        print(f"dodge {name} preclick: {(time.time()-self.start_time)/0.03333}")
        print(f"expected: {expected_time}")
        pyautogui.leftClick()
        pyautogui.press("ctrl")

    def try_dodge(self):
        if (not self.finished_dodging):
            if (self.active_enemy_is_walking):

                if (not self.finished_barrel):
                    barrel_dodge_time = BARREL_TIMING + WALK_DELAYS[self.active_enemy_position] + SAFETY_OFFSET
                    if (time_has_passed(self.start_time, barrel_dodge_time)):
                        self.do_dodge("barrel", barrel_dodge_time)
                        self.finished_barrel = True #after dodging barrel, dont do it again

                single_dodge_time = SINGLE_TIMING + WALK_DELAYS[self.active_enemy_position] + SAFETY_OFFSET
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
    
    def check_health_bars(self, frame):
        for i in range(4):
            color = get_pixel(frame, *HEALTH_POSES[i])
            bar_visible = color == HEALTH_RED or color == HEALTH_YELLOW 
            self.in_place_health_bars[i] = bar_visible

    def check_walk(self):
        if (self.waiting_to_check_walking):
            if (time_has_passed(self.start_time, ENEMY_MOVE_TIME)):
                self.waiting_to_check_walking = False
                if (self.in_place_health_bars[self.active_enemy_position] == True):
                    print("enemy not walking")
                else:
                    self.active_enemy_is_walking = True
                    print("detected enemy walking")
    
