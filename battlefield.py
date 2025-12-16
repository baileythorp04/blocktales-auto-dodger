from helpers import *

class Battlefield():
    enemy_places = [False, False, False, True]
    attacks_done_this_turn = 0

    def __init__(self):
        doing_pit = False
        if (doing_pit):
            self.enemy_places = ["trotter", "trotter", "trotter", "empty"] 
        else:
            self.enemy_places = ["empty", "empty", "empty", "trotter"] 

    def get_next_enemy_position(self):

        attack_counter = 0
        for i, enemy in enumerate(self.enemy_places):
            if (enemy == "trotter"):
                attack_counter += 2
            elif (enemy == "ghost"):
                attack_counter += 1
            
            if (attack_counter > self.attacks_done_this_turn):
                self.attacks_done_this_turn += 1
                return i
            
        #failsafe
        self.attacks_done_this_turn += 1
        return 3 


