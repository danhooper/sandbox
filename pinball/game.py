from pinball import components, rules
import procgame
from procgame import *


class Game(game.BasicGame):

    def __init__(self):
        super(Game, self).__init__("wpc")
        self.sound = sound.SoundController(self)
        self.settings = {}

    def setup(self):
        self.load_config("config/machine.yaml")
        self.load_game_data("config/defaults.yaml", "var/game.yaml")

        self.font_tiny    = dmd.font_named("04B-03-7px.dmd")
        self.font_9x7     = dmd.font_named("Font09x7.dmd")
        self.font_bold    = dmd.font_named("Font09Bx7.dmd")
        self.font_14x10   = dmd.font_named("Font14x10.dmd")
        self.font_18x11   = dmd.font_named("Font18x11.dmd")
        self.font_jazz    = dmd.font_named("Jazz18-18px.dmd")

        self.sound.register_sound("service_enter",       "sounds/menu_in.wav")
        self.sound.register_sound("service_exit",        "sounds/menu_out.wav")
        self.sound.register_sound("service_next",        "sounds/next_item.wav")
        self.sound.register_sound("service_previous",    "sounds/previous_item.wav")
        self.sound.register_sound("service_switch_edge", "sounds/switch_edge.wav")
        self.sound.register_sound("service_save",        "sounds/save.wav")
        self.sound.register_sound("service_cancel",      "sounds/cancel.wav")
        self.service_mode = service.ServiceMode(self,100,self.font_tiny,[])

        self.mode = components.Modes(self)
        #self.score_display_mode = procgame.modes.ScoreDisplay(self, 0)
        self.reset()

    def reset(self):
        super(Game, self).reset()
        self.modes.add(self.mode.attract)

    def create_player(self, name):
        return rules.Player(name)

    def set_status(self, text):
        self.dmd.set_message(text, 3)
        print(text)

    def game_ended(self):
        super(Game, self,).game_ended()
        self.modes.remove(self.mode.base)
        self.modes.add(self.mode.attract)
