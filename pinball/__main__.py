import locale
from pinball.game import Game

def main():
    locale.setlocale(locale.LC_ALL, "")
    game = Game()
    try:
        game.setup()
        game.run_loop()
    finally:
        del game

if __name__ == "__main__":
    main()
