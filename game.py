from battleground import Battleground
from available_characters import characters_dict


class Game:
    def __init__(self):
        self.turn = 0
        self.winner = None
        self.current_player = None
        self.battleground = None
        self.available_characters = list(characters_dict.keys())
        self.max_characters = 1
        self.player_win = False


    def play_game(self):
        self.init_game(predefined_characters=True)
        while not self.player_win:
            self.play_one_turn()
            self.check_if_player_win()

    def init_game(self,  team_a="A", team_b="B", scenario="Default", predefined_characters=False):
        self.battleground = Battleground(scenario, team_a, team_b)
        if predefined_characters:
            team_a_characters = ["Wurk"]
            team_b_characters = ["Katriona"]
        else:
            team_a_characters = self.select_team_characters(team_a)
            team_b_characters = self.select_team_characters(team_b)
        self.battleground.add_players_to_team(team_a_characters, 1)
        self.battleground.add_players_to_team(team_b_characters, 2)

    def select_team_characters(self, team):
        characters_selected = []
        while len(characters_selected) < self.max_characters:
            print("\n==========================")
            print("Select characters of team " + team)
            print("Available characters: ")
            for character in self.available_characters:
                print("-> {}".format(character))
            character_selected = input("Select character name: ")
            if character_selected in self.available_characters:
                print("Character selected: " + character_selected)
                print("1 -> Confirm selection")
                print("2 -> Show character info")
                print("3 -> back to select character")
                option = int(input("Select option: "))
                if option == 1:
                    print("Character selected: " + character_selected)
                    characters_selected.append(character_selected)
                    self.available_characters.remove(character_selected)
                elif option == 2:
                    print("Character info")
                    print(characters_dict[character_selected].get_info())
                elif option == 3:
                    continue
            else:
                print("Invalid character")
        return characters_selected

    def select_current_player(self):
        if not self.current_player:
            self.current_player = 1
        else:
            self.current_player = 1 if self.current_player == 2 else 2

    def player_win(self):
        pass

    def play_one_turn(self):
        self.turn += 1
        self.select_current_player()
        print("\nTEAM " + self.battleground.teams[self.current_player].name.upper() + " IS YOUR TURN")
        available_characters = self.battleground.teams[self.current_player].get_characters().copy()
        while len(list(available_characters.keys())) > 0:
            print("================================")
            print("Your available characters")
            self.battleground.show_team_characters(available_characters)
            print("================================\n")
            character_input = int(input("Select character to play: "))
            if character_input < 1 or character_input > len(list(available_characters.keys())):
                print("Invalid character")
                continue

            character_selected = available_characters[character_input]
            self.battleground.perform_action_with_character(character_selected, self.current_player)
            available_characters.pop(character_input)


    def check_if_player_win(self):
        team_a_characters = self.battleground.teams[1].get_characters()
        team_b_characters = self.battleground.teams[2].get_characters()
        if len(team_a_characters) == 0:
            self.winner = self.battleground.teams[2].name
            self.player_win = True
        elif len(team_b_characters) == 0:
            self.winner = self.battleground.teams[1].name
            self.player_win = True
        return self.player_win

        


            




















