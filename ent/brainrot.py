class BrainRot:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    @classmethod
    def get(cls):
        brainrots = [
            cls("tralalero tralala","gold"),
            cls("tung tung sahur","diamond"),
            cls("lirililarila","plate"),
            cls("bombardiro", "gold"),
            cls("tralalero tralala", "gold"),
            cls("tung tung sahur", "diamond"),
            cls("lirililarila", "plate"),
            cls("bombardiro", "gold")

        ]
        return brainrots