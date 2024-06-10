from characters.base_character import BaseCharacter


class Wizard(BaseCharacter):
    def __init__(self, name, character_data):
        super().__init__(name, character_data)
        self.mana = 1000

    def apply_class_stats(self):
        self.special_attack += 100
        self.special_defense += 20
        self.actions.append(self.create_magic)

    def create_magic(self, team_members):
        for member in team_members:
            member.special_aatack += 50
            self.special_attack += 50
