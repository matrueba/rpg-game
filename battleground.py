from team import Team
from available_characters import characters_dict


class Battleground:

    def __init__(self, name, team_a, team_b):
        self.name = name
        self.teams = {
            "A": Team(team_a),
            "B": Team(team_b)
        }

    def add_players_to_team(self, characters, team):
        try:
            for character in characters:
                if character in characters_dict.keys():
                    character_created = characters_dict[character]
                    self.teams[team].add_player(character_created)
        except Exception as e:
            print(e)

    def show_team_characters(self, characters):
        try:
            for key, character in characters.items():
                print(key + " ===> " + character.name)
        except Exception as e:
            print(e)

    def show_character_actions(self, character):
        try:
            for key, action in character.get_actions().items():
                print(key + " ===> " + action.get_action_info()["name"])
        except Exception as e:
            print(e)

    def select_action_target(self, team):
        # If action is health select same team
        print("\n=======================")
        print("Select target")
        if team == "A":
            target_team = "B"
        else:
            target_team = "A"
        target_team_characters = self.teams[target_team].characters
        self.show_team_characters(target_team_characters)
        print("=======================")
        target_character = int(input("Select target: "))
        if target_character < 1 or target_character > len(list(target_team_characters.keys())):
            print("Invalid character")
            return
        target = self.teams[target_team].characters[str(target_character)]
        return target

    def perform_action_with_character(self, available_characters, character_selected, team):
        character = available_characters[str(character_selected)]
        print("\n=========================")
        print("Available actions: ")
        self.show_character_actions(character)
        print("=========================: ")
        action_input = int(input("Select action: "))
        action_selected = character.get_actions()[str(action_input)]
        target = self.select_action_target(team)
        self.run_action_player(action_selected, character, target)

    def run_action_player(self, action, character, target):
        action.perform(character, target)
        #self.claculate_stats()






