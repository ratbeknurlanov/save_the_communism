from game import Game


FIELD_WIDTH = 5500
FIELD_HEIGHT = 1024

def main():
    game = Game('Save The Communism', "images/main_background.png", 30, FIELD_WIDTH, FIELD_HEIGHT)
    game.init()
    game.run()


if __name__ == '__main__':
    main()
