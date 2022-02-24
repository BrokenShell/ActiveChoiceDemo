from active_choice import ActiveChoice
from game import run_game


player_1 = ActiveChoice("Player 1", ("lizard", "scissors", "rock", "paper", "spock"))
player_2 = ActiveChoice("Player 2", ("rock",))


print("\n# Pre Game")
print(player_1)
print(player_2)

run_game(player_1, player_2, cycles=10000)

print("\n# Final Scores")
print(player_1)
print(player_2)
