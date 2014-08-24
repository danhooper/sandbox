import procgame

class Player(procgame.game.Player):

    bumper_value = 100
    super_jets_value = 1000
    slingshot_value = 10

    def __init__(self, name):
        super(Player, self).__init__(name)
        self.super_jets = False

    def bumper(self):
        if self.super_jets:
            self.score += self.super_jets_value
        else:
            self.score += self.bumper_value

    def slingshot(self):
        self.score += self.slingshot_value

    def end_of_turn(self):
        self.super_jets = False
