from characters.classes.warrior import Warrior
from actions.action import Action
import random


class AmazonPride(Action):

    def __init__(self):
        self.name = "Amazon Pride"
        self.action_category = "attack"
        self.action_type = "physical"
        self.description = ""
        self.attack = None
        super().__init__(self.name, self.action_category, self.action_type, self.description)

    def character_current_stats(self, stats):
        self.attack = stats["attack"]
        

    def perform(self, character, target):
        action_stats = self.action_stats.copy()
        action_stats["hit_power"] = 0
        action_stats["damage"] = 0
        hit_power = int((character.attack * random.uniform(0, 1) + 100) - target.defense * random.uniform(0, 1))
        action_stats["hit_power"] = hit_power
        damage = hit_power - target.defense * 0.5
        action_stats["damage"] = damage
        target.current_health = target.current_health - damage
        return action_stats


class Katriona(Warrior):
    def __init__(self):
        character_data = {
            "health": 1000,
            "attack": 60,
            "special_attack": 250,
            "defense": 30,
            "special_defense": 120
        }
        super().__init__("Katriona", character_data)
        self.actions = {
            1: AmazonPride()
        }


