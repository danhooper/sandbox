from procgame import *

class Mode(game.Mode):
    def __init__(self, game):
        super(Mode, self).__init__(game, 1)

        highscore_categories = []
        cat = highscore.HighScoreCategory()
        cat.game_data_key = "HighScores"
        cat.titles = [
            "Grand Champion",
            "High Score 1",
            "High Score 2",
            "High Score 3",
            "High Score 4"
        ]
        highscore_categories.append(cat)
        for category in highscore_categories:
            category.load_from_game(game)

        frame_proc = dmd.Animation().load('dmd/P-ROC.dmd').frames[0]
        layer_proc = dmd.FrameLayer(opaque=True, frame=frame_proc)
        layer_th = dmd.TextLayer(128/2, 7, game.font_jazz, "center",
                opaque=True).set_text("Town Hall")
        layer_presents = dmd.TextLayer(128/2, 7, game.font_jazz, "center",
                opaque=True).set_text("Presents")
        layer_name = dmd.TextLayer(128/2, 7, game.font_jazz, "center",
                opaque=True).set_text("TBD")
        layer_high_scores = []
        for frame in highscore.generate_highscore_frames(highscore_categories):
            layer_high_scores.append(dmd.FrameLayer(opaque=True, frame=frame))
        self.layer = dmd.ScriptedLayer(128, 32, [
            { "layer": None,                  "seconds": 10.0 },
            { "layer": layer_proc,            "seconds": 3.0 },
            { "layer": layer_th,              "seconds": 3.0 },
            { "layer": layer_presents,        "seconds": 3.0 },
            { "layer": layer_name,            "seconds": 3.0 },
            { "layer": layer_high_scores[0],  "seconds": 3.0 },
            { "layer": layer_high_scores[1],  "seconds": 3.0 },
            { "layer": layer_high_scores[2],  "seconds": 3.0 },
            { "layer": layer_high_scores[3],  "seconds": 3.0 },
            { "layer": layer_high_scores[4],  "seconds": 3.0 },
        ])

    def mode_stopped(self):
        self.layer.script_index = 0
        self.frame_start_time = None
        self.is_new_script_item = True

    def sw_enter_active(self, sw):
        self.game.modes.add(self.game.service_mode)
        return True

    def sw_exit_active(self, sw):
        return True

    def sw_startButton_active(self, sw):
        self.game.modes.remove(self)
        self.game.modes.add(self.game.mode.base)
        return True
