from team import Team
from available_characters import characters_dict


class Battleground:

    def __init__(self, name, team_a, team_b):
        self.name = name
        self.teams = {
            1: Team(team_a),
            2: Team(team_b)
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
                print(str(key) + " ===> " + character.name)
        except Exception as e:
            print(e)

    def show_character_actions(self, character):
        try:
            for key, action in character.get_actions().items():
                print(str(key) + " ===> " + action.get_action_info()["name"])
        except Exception as e:
            print(e)

    def select_action_target(self, team):
        # If action is health select same team
        print("\n=======================")
        print("Select target")
        target_team = self.target_team(team)
        if team == 1:
            target_team_characters = self.teams[target_team].characters
        else:
            target_team_characters = self.teams[target_team].characters
        self.show_team_characters(target_team_characters)
        print("=======================\n")
        target_character = int(input("Select target: "))
        if target_character < 1 or target_character > len(list(target_team_characters.keys())):
            print("Invalid character")
            return
        target = target_team_characters[target_character]
        return target

    def perform_action_with_character(self, character, team):
        print("\n=========================")
        print("Character selected: " + character.name)
        print("Available actions: ")
        self.show_character_actions(character)
        print("=========================\n")
        action_input = int(input("Select action: "))
        action_selected = character.get_actions()[action_input]
        target = self.select_action_target(team)
        action_stats = self.run_action_player(action_selected, character, target)
        target_team = self.target_team(team)
        if self.check_character_defeated(target):
            print(target.name + " is defeated")
            self.teams[target_team].characters.pop(target.name)
        self.print_action_stats(character, target, action_stats)



    def run_action_player(self, action, character, target):
        action_stats = action.perform(character, target)
        return action_stats


    def check_character_defeated(self, character):
        if character.current_health <= 0:
            return True
        return False
    
    def print_action_stats(self, character, target, action_stats):
        print("\n=========================")
        print("Action stats")
        print (character.name + " perform " + action_stats["name"] + " over " + target.name + "\n")
        print("Hit power: " + str(action_stats["hit_power"]))
        print("Damage: " + str(action_stats["damage"]))
        print("Health recovered: " + str(action_stats["health_recovered"]))
        print("Mana recovered: " + str(action_stats["mana_recovered"]) + "\n")
        print(character.name + " stats")
        print(character.get_info())
        print(target.name + " stats")
        print(target.get_info())
        print("=========================\n")



    def target_team(self, team):
        if team == 1:
            return 2
        return 1


