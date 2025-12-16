import pyautogui
import time
import dxcam
from menu import Menu
from dots import Dots
from dodged_state import Dodged_State
from helpers import check_for_menu
from constants import *

#the default 0.1s pause only applies after theq click so it is(n't) problem ???
pyautogui.PAUSE = 0






#########################
##### START OF CODE #####
#########################
cam = dxcam.create()
cam.start()
try:

    ### STATE ###
    
    timer = time.time()

    dodging_walk_attacks = True #to be integrated into Dodged_State once helathbar vision is added
    menu_open = False

    menu = Menu()
    dots = Dots()
    dodger = Dodged_State()


    while True:
        ### first, see if you need to dodge ###
        dodger.try_dodge()


        ### scan all pixels before logic ###
        frame = cam.get_latest_frame()
        if frame is None:
            continue
        menu_open = check_for_menu(frame)
        dots.scan_dots(frame)
        dodger.check_walk(frame)

        ### get time since last time screen was read ###
        new_time = time.time()
        #print(f"loop took: {new_time - timer}")
        timer = new_time
    
        ### choose if menu should open or close ###
        res = menu.set_openness(menu_open)
        if (res == "just opened"):
            dots.reset()
            dodger.disable()
        if (not menu.is_open):
            
            ### actual logic ###
            if (dots.check_for_dot_change()):
                print("time started")
                dodger.enable()


            
except KeyboardInterrupt:
    pass
finally:
    cam.stop()


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