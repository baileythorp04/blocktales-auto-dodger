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
        print("ran out of enemies. giving last position")
        self.attacks_done_this_turn += 1
        return 3 

    def remove_enemy(self, pos):
        if (self.enemy_places[pos] != "empty"):
            print(f"removed {self.enemy_places[pos]} from position {pos}")
            self.enemy_places[pos] = "empty"
        else:
            print(f"couldn't remove. no enemy in position {pos}")
        print(f"battlefield is now {self.enemy_places}")

    def add_ghost(self, pos):
        if (self.enemy_places[pos] == "empty"):
            print(f"added ghost to position {pos}")
            self.enemy_places[pos] = "ghost"
        else:
            print(f"couldn't summon, {self.enemy_places[pos]} already at position {pos}")
        print(f"battlefield is now {self.enemy_places}")
        
