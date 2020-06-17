class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        pass

    def comparator(self, other):
        if self.score > other.score:
            return -1
        if self.score < other.score:
            return 1
        if self.score == other.score:
            if self.name < other.name:
                return -1
            if self.name > other.name:
                return 1
            if self.name == other.name:
                return 0

