from battleground import Battleground
from available_characters import characters_dict


class Game:
    def __init__(self):
        self.turn = 0
        self.winner = None
        self.current_player = None
        self.battleground = None
        self.available_characters = list(characters_dict.keys())
        self.player_win = False

    def play_game(self):
        self.init_game()
        if not self.player_win:
            self.play_one_turn()

    def init_game(self):
        self.battleground = Battleground("jungle", "loquillos", "los nanos")
        team_a_characters = self.select_team_characters("A")
        team_b_characters = self.select_team_characters("B")
        self.battleground.add_players_to_team(team_a_characters, "A")
        self.battleground.add_players_to_team(team_b_characters, "B")

    def select_team_characters(self, team):
        characters_selected = []
        print("\n==========================")
        print("Select characters of team " + team)
        print("Available characters: ")
        for character in self.available_characters:
            print("-> {}".format(character))
        character_selected = input("Select character name: ")
        if character_selected in self.available_characters:
            characters_selected.append(character_selected)
            self.available_characters.remove(character_selected)
        return characters_selected

    def select_current_player(self):
        if not self.current_player:
            self.current_player = "A"
        if self.current_player == "A":
            self.current_player = "B"
        if self.current_player == "B":
            self.current_player = "A"

    def player_win(self):
        pass

    def play_one_turn(self):
        self.turn += 1
        self.select_current_player()
        print("\nTEAM " + self.battleground.teams[self.current_player].name.upper() + " IS YOUR TURN")
        available_characters = self.battleground.teams[self.current_player].get_characters()
        while len(list(available_characters.keys())) > 0:
            print("\n================================")
            print("Your available characters")
            self.battleground.show_team_characters(available_characters)
            print("================================")
            character_input = int(input("Select character to play: "))
            if character_input < 1 or character_input > len(list(available_characters.keys())):
                print("Invalid character")
                continue
            self.battleground.perform_action_with_character(available_characters, character_input, self.current_player)
            available_characters.pop(str(character_input))


















