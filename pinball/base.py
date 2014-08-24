from procgame import *

class Mode(game.Mode):
    def __init__(self, game):
        super(Mode, self).__init__(game, 1)
        self.score_display = modes.ScoreDisplay(game, 0)

    def p(self):
        return self.game.current_player()

    def mode_started(self):
        self.game.start_game()
        self.game.add_player()
        self.game.start_ball()
        self.game.modes.add(self.score_display)

    def sw_startButton_active(self, sw):
        if len(self.game.players) < 4 and self.game.ball == 1:
            self.game.add_player()
        return True

    def sw_drain_active(self, sw):
        self.p().end_of_turn()
        self.game.end_ball()
        self.game.start_ball()
        return True

    def sw_bumper_active(self, sw):
        self.p().bumper()
        return True

    def sw_slingshot_active(self, sw):
        self.p().slingshot()
        return True

    def sw_superJets_active(self, sw):
        self.p().super_jets = True
        return True
