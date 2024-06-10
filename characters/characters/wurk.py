from characters.classes.wizard import Wizard
from actions.action import Action
import random


class ForbiddenRite(Action):

    def __init__(self):
        self.name = "Forbidden Rite"
        self.action_category = "attack"
        self.action_type = "special"
        self.description = ""
        self.special_attack = None
        super().__init__(self.name, self.action_category, self.action_type, self.description)

    def character_current_stats(self, stats):
        self.special_attack = stats["special_attack"]

    def perform(self, character, target):
        hit_power = None
        if character.mana >= 100:
            hit_power = self.special_attack * 0.5 + 100
            character.mana -= 100
        return hit_power


class MagicRecovery(Action):

    def __init__(self):
        self.name = "Magic Recovery"
        self.action_category = "spell"
        self.action_type = "special"
        self.description = ""
        self.special_attack = None
        super().__init__(self.name, self.action_category, self.action_type, self.description)

    def character_current_stats(self, stats):
        self.special_attack = stats["special_attack"]

    def perform(self, character, target):
        target.current_health += target.max_health * 0.2
        if target.current_health > target.max_health:
            target.current_health = target.max_health


class Wurk(Wizard):
    def __init__(self):
        character_data = {
            "health": 10000,
            "attack": 60,
            "special_attack": 250,
            "defense": 30,
            "special_defense": 120
        }
        super().__init__("Wurk", character_data)
        self.mana = 1600
        self.actions = {
            "1": ForbiddenRite(),
            "2": MagicRecovery()
        }

    def dark_staff(self):
        hit_power = self.attack * random.choice([0.5, 0.6, 0.7, 0.8])
        return hit_power, "physical"


    # def power_of_evil(self, player):
    #     player.special_attack += 100
    #     self.mana -= 80




