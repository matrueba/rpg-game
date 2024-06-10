from collections import OrderedDict


class Team:
    def __init__(self, name):
        self.name = name
        self.characters = OrderedDict()

    def add_player(self, player):
        len_characters = len(list(self.characters.keys()))
        self.characters[str(len_characters + 1)] = player

    def get_characters(self):
        return self.characters
