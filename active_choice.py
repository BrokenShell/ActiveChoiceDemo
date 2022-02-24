from Fortuna import RelativeWeightedChoice


class ActiveChoice:

    def __init__(self, name, data, start=50, lo=1, hi=100):
        self.name = name
        self.raw_data = {k: start for k in data}
        self.start = start
        self.lo = lo
        self.hi = hi
        self.data = self.build()
        self.wins = 0
        self.losses = 0

    def __call__(self):
        return self.data()

    def build(self):
        return RelativeWeightedChoice(
            zip(self.raw_data.values(), self.raw_data.keys())
        )

    def winner(self, result):
        self.wins += 1
        if self.raw_data[result] < self.hi:
            self.raw_data[result] += 1
            self.data = self.build()

    def loser(self, result):
        self.losses += 1
        if self.raw_data[result] > self.lo:
            self.raw_data[result] -= 1
            self.data = self.build()

    def win_ratio(self):
        total_games = self.wins + self.losses
        return self.wins / total_games if total_games else total_games

    def __str__(self):
        max_weight = max(self.raw_data.values())
        output = (
            f"{self.name}: {self.raw_data}",
            f"Best strategies: " + ", ".join(
                k for k, v in self.raw_data.items() if v == max_weight),
            f"Win Rate: {self.win_ratio():.2%}",
            ""
        ) if self.win_ratio() else (f"{self.name}: {self.raw_data}", "")
        return "\n".join(output)
