def run_game(player_1, player_2, cycles=1000):

    game_rules = {
        "rock": {"rock": 0, "paper": -1, "scissors": 1, "lizard": 1, "spock": -1},
        "paper": {"rock": 1, "paper": 0, "scissors": -1, "lizard": -1, "spock": 1},
        "scissors": {"rock": -1, "paper": 1, "scissors": 0, "lizard": 1, "spock": -1},
        "lizard": {"rock": -1, "paper": 1, "scissors": -1, "lizard": 0, "spock": 1},
        "spock": {"rock": 1, "paper": -1, "scissors": 1, "lizard": -1, "spock": 0},
    }

    def game():
        a = player_1()
        b = player_2()
        this_game = game_rules[a][b]
        if this_game > 0:
            player_1.winner(a)
            player_2.loser(b)
        elif this_game < 0:
            player_1.loser(a)
            player_2.winner(b)
        else:
            player_1.loser(a)
            player_2.loser(b)

    for _ in range(cycles):
        game()
