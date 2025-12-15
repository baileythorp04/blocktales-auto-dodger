import time
import pyautogui
from colorist import ColorRGB, BgColorRGB
import keyboard

#the default 0.1s pause only applies after the click so it is(n't) problem ???
pyautogui.PAUSE = 0

LOG_GRAY = (195, 200, 200)
HEALTH_YELLOW = (216, 164, 21) 
HEALTH_YELLOW_DARK = () 
HEALTH_YELLOW_DARKER = () 
HEALTH_RED = (201, 55, 15)
HEALTH_RED_DARK = ()
HEALTH_RED_DARKER = ()
SWORD_GREEN = (84, 161, 104) 
MENU_BALL_PURPLE = (204, 41, 188)

LOG_DOT_POSES = ((468, 67),
(468, 103),
(468, 139),
(468, 175))
HEALTH_1_POS = (1210,648)
HEALTH_2_POS = (1360,648)
HEALTH_3_POS = (1505,648)
HEALTH_4_POS = (1640,648)
SWORD_START_POS = (703, 745)
SWORD_END_POS = (1216, 745)
MENU_BALL_POS = (125,115)

BARREL_TIMING = 91
SINGLE_TIMING = 112
TRIPLE_1_TIMING =  82
TRIPLE_2_TIMING = 97
TRIPLE_3_TIMING = 109

DELAY_1 = 0
DELAY_2 = 1
DELAY_3 = 4
DELAY_4 = 9



def sleep_frames(frames):
    time.sleep(frames * 0.03333)

def time_has_passed(start_time, frames):
    end_time = start_time + (frames*0.03333)
    return time.time() >= end_time

class Dots:
    dots = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]

    def reset():
        dots = [(0,0,0), (0,0,0), (0,0,0), (0,0,0)]


    def check_for_dot_change(self):
        for i in range(4):
            new_color = pyautogui.pixel(*LOG_DOT_POSES[i])
            if (self.dots[i] != new_color): #update each dot to the newest color
                self.dots[i] = new_color
                if (new_color == LOG_GRAY): 
                    #separate into two logic trees: 4th dot is background color or not
                    #detect 4th dot by: text disappears but dot is still white

                    if (i == 0):
                        print("player's dot found")
                    else:
                        print("dot found")
                        return True

class Dodged_State():
    start_time = 0
    finished_dodging = True
    finished_barrel = True


    def enable(self):
        start_time = time.time()
        finished_barrel = False
        finished_dodging = False



    def disable(self):
        finished_dodging = True


    def do_dodge(self):

        if (not self.finished_barrel):
            if (time_has_passed(self.start_time, BARREL_TIMING + DELAY_4 + safety_offset)):
                dodged_barrel = True
                print(f"dodge barrel preclick: {(time.time()-self.start_time)/0.03333}")
                pyautogui.leftClick()
                #print(f"dodge barrel : {(time.time()-self.start_time)/0.03333}")

                self.finished_barrel = True #after dodging barrel, dont do it again


        if (time_has_passed(self.start_time, SINGLE_TIMING + DELAY_4 + safety_offset)):
            dodged_single = True
            print(f"dodge single preclick: {(time.time()-self.start_time)/0.03333}")
            pyautogui.leftClick()
            #print(f"dodge single: {(time.time()-self.start_time)/0.03333}")

            self.finished_dodging = True #after dodging single, stop dodging

def check_for_menu():
    return pyautogui.pixel(*MENU_BALL_POS) == MENU_BALL_PURPLE
        

def wait_for_player():
    print("press q to continue")
    keyboard.wait('q')
    print("started looking for dot")



#########################
##### START OF CODE #####
#########################


### SETTINGS ###
safety_offset = -3
time_waiting_for_enemy_to_highlight = 4
time_waiting_for_enemy_to_move = time_waiting_for_enemy_to_highlight + 10

### STATE ###
dodging_walk_attacks = True #to be integrated into Dodged_State once helathbar vision is added

dots = Dots()
dodged_state = Dodged_State()

wait_for_player()

while True:

    if (check_for_menu()):
        print("menu open")
        dots = Dots()
        dodged_state.disable()
        wait_for_player()
        

    if (dots.check_for_dot_change()):
        print("time started")
        dodged_state.enable()

    dodged_state.do_dodge()

    



# wait to be armed (on button press for now)
# wait for white dot to appear in log
# wait until dodge time
# click




# dodge time is either for barrel and single (health bar moves)
# or triple (health bar always overlap original position)

# a delay is added to barrel and single depending on position (#th enemy firing that turn)




#### final ####

#start as player's turn
#select player action
#wait for dot
#do ball/sword minigame
#wait for menu
#select action
#wait for dot
#do ball/sword minigame


#loop for each enemy
    #do twice for each enemy except ghost
        #wait for dot
        #start counting time for enemy dodge
        #wait ~3 frames for health bar to get into place
        #continually check if health bar is still there
            #if so, dodge for triple + delay
            #else, dodge for single and barrel + delay

#at any time if the menu appears, stop and to back to player's turn


#remember:
#prepare makes the camera zoom in. it takes time for it to zoom back out (though it will always be barrel so shouldn't matter)
#it takes ~3 frames for trotter to get to normal position after dot
#only concern for detecting walking is #2. it takes 13 frames to walk fully for barrel