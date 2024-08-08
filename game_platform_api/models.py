class Choices:
    def __init__(self, choices: list[str]):
        self.choices = choices
        self.count_rounds = len(choices)

    def get_data(self) -> str:
        formatted_choices = []
        for i, choice in enumerate(self.choices, start=1):
            formatted_choices.append(f"round{i}:{choice}")
        return ','.join(formatted_choices)

class Room:
    def __init__(self, wallet_creator, name_room, id_room):
        self.wallet_creator = wallet_creator
        self.name_room = name_room
        self.id_room = id_room

class Game:
    def __init__(self, game_id, room_id, player, choice, bet, winner, disc):
        self.game_id = game_id
        self.room_id = room_id
        self.player = player
        self.choice = choice
        self.bet = bet
        self.winner = winner
        self.disc = disc

    def __str__(self):
        return (f"Game ID: {self.game_id}\n"
                f"Room ID: {self.room_id}\n"
                f"Player: {self.player}\n"
                f"Choice: {self.choice}\n"
                f"Bet: {self.bet}\n"
                f"Winner: {self.winner}\n"
                f"Result: {self.disc}\n")
    
    