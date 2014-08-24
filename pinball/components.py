from pinball import attract, base

class Modes(object):

    def __init__(self, game):
        self.attract = attract.Mode(game)
        self.base = base.Mode(game)
