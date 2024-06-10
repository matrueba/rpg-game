

class BaseCharacter:
    def __init__(self, name, character_data):
        self.name = None
        self.max_health = 0
        self.current_health = 0
        self.attack = 0
        self.special_attack = 0
        self.defense = 0
        self.special_defense = 0
        self.actions = {}
        self.initial_stats = character_data
        self.initialize_character(name, character_data)

    def initialize_character(self, name, character_data):
        self.name = name
        self.max_health = character_data["health"]
        self.current_health = character_data["health"]
        self.attack = character_data["attack"]
        self.special_attack = character_data["special_attack"]
        self.defense = character_data["defense"]
        self.special_defense = character_data["special_defense"]

    def attack(self, action_selected):
        if self.actions:
            for action in self.actions:
                if action == action_selected:
                    action.__call__()

    def clear(self):
        self.initialize_character(self.name, self.initial_stats)

    def get_name(self):
        return self.name

    def get_actions(self):
        return self.actions
    
    def get_info(self):
        for key, value in self.__dict__.items():
            if key != "actions" and key != "initial_stats" and key != None:      
                print(key.replace('_', ' ') + " => " + str(value))
