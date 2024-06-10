class Action:
    def __init__(self, name, action_category, action_type, description):
        self.name = name
        self.action_category = action_category
        self.action_type = action_type
        self.description = description

    def perform(self, character, target):
        pass

    def get_action_info(self):
        return self.__dict__


