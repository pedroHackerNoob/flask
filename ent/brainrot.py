class BrainRot:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    @classmethod
    def get(cls):
        brainrots = [
            cls("tralalero tralala","gold"),
            cls("tung tung sahur","gold"),
            cls("lirililarila","gold")
        ]
        return brainrots