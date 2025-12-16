import time
import keyboard
import pyautogui
from constants import *

def time_has_passed(start_time, frames):
    end_time = start_time + (frames*0.03333)
    return time.time() >= end_time


def check_for_menu():
    return pyautogui.pixel(*MENU_BALL_POS) == MENU_BALL_PURPLE
        

def wait_for_player():
    print("press q to continue")
    keyboard.wait('q')
