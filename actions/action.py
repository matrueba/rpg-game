class Action:
    def __init__(self, name, action_category, action_type, description):
        self.name = name
        self.action_category = action_category
        self.action_type = action_type
        self.description = description
        self.action_stats = {
            "name": self.name,
            "hit_power": 0,
            "damage": 0,
            "health_recovered": 0,
            "mana_recovered": 0
        }

    def perform(self, character, target):
        action_stats = {}
        return action_stats

    def get_action_info(self):
        return self.__dict__
    
    


