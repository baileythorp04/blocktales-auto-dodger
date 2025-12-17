from helpers import *

class Battlefield():
    enemy_places = ["trotter", "trotter", "trotter", "empty"] 
    attacks_done_this_turn = 0

    def reset_attacks(self):
        self.attacks_done_this_turn = 0

    def get_next_enemy_position(self):

        attack_counter = 0
        for i, enemy in enumerate(self.enemy_places):
            if (enemy == "trotter"):
                attack_counter += 2
            elif (enemy == "ghost"):
                attack_counter += 1
            
            if (attack_counter > self.attacks_done_this_turn):
                self.attacks_done_this_turn += 1
                print(f"dodging enemy position: {i}")
                return i
            
        #failsafe
        self.attacks_done_this_turn += 1
        return 3 


