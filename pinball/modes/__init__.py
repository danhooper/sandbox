import pinball.modes as m

class All(object):

    def __init__(self, game):
        self.attract = m.attract.Mode(game)
