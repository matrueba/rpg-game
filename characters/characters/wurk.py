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
        action_stats = self.action_stats.copy()
        action_stats["hit_power"] = 0
        action_stats["damage"] = 0
        if character.current_mana >= 100:
            hit_power = character.special_attack * random.choice([0.4, 0.5, 0.6, 0.7, 0.8]) + 100
            character.current_mana -= 100
            damage = hit_power - target.special_defense * 0.5
            target.current_health -= damage
            action_stats["hit_power"] = hit_power
            action_stats["damage"] = damage
        return action_stats


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
            "health": 800,
            "attack": 60,
            "special_attack": 250,
            "defense": 30,
            "special_defense": 120
        }
        super().__init__("Wurk", character_data)
        self.mana = 1200
        self.current_mana = 1200
        self.actions = {
            1: ForbiddenRite(),
            2: MagicRecovery()
        }

    def dark_staff(self):
        hit_power = self.attack * random.choice([0.5, 0.6, 0.7, 0.8])
        return hit_power, "physical"


    # def power_of_evil(self, player):
    #     player.special_attack += 100
    #     self.mana -= 80




