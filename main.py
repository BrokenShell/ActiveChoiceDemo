from active_choice import ActiveChoice
from game import run_game


player_1 = ActiveChoice("Player 1", ("rock", "paper", "scissors", "lizard", "spock"))
player_2 = ActiveChoice("Player 2", ("rock", "paper", "scissors"))


print("\n# Pre Game")
print(player_1)
print(player_2)

run_game(player_1, player_2, cycles=1000)

print("\n# Final Scores")
print(player_1)
print(player_2)
