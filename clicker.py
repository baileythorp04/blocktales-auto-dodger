import pyautogui
import time
import dxcam
from keyboard import add_hotkey
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

    add_hotkey("ctrl+1", dodger.field.remove_enemy, args=[0])
    add_hotkey("ctrl+2", dodger.field.remove_enemy, args=[1])
    add_hotkey("ctrl+3", dodger.field.remove_enemy, args=[2])
    add_hotkey("ctrl+4", dodger.field.remove_enemy, args=[3])
    add_hotkey("shift+1", dodger.field.add_ghost, args=[0])
    add_hotkey("shift+2", dodger.field.add_ghost, args=[1])
    add_hotkey("shift+3", dodger.field.add_ghost, args=[2])
    add_hotkey("shift+4", dodger.field.add_ghost, args=[3])

    while True:
        ### first, see if you need to dodge ###
        dodger.try_dodge()


        ### scan all pixels before logic ###
        frame = cam.get_latest_frame()
        if frame is None:
            continue
        menu_open = check_for_menu(frame)
        dots.scan_dots(frame)
        dodger.check_health_bars(frame)
        

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
            
            dodger.check_walk()


            
except KeyboardInterrupt:
    pass
finally:
    cam.stop()