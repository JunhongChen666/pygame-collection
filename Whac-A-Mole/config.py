import os


SCREENSIZE = (993, 477)


ROOTDIR = os.getcwd()

GAME_BG_IMAGEPATH = os.path.join(ROOTDIR, 'resources/images/background.png')
HAMMER_IMAGEPATHS = [os.path.join(ROOTDIR, 'resources/images/hammer0.png'), os.path.join(ROOTDIR, 'resources/images/hammer1.png')]
MOLE_IMAGEPATHS = [
    os.path.join(ROOTDIR, 'resources/images/mole_1.png'), 
    os.path.join(ROOTDIR, 'resources/images/mole_laugh1.png'),
    os.path.join(ROOTDIR, 'resources/images/mole_laugh2.png'), 
    os.path.join(ROOTDIR, 'resources/images/mole_laugh3.png')
]
FONT_PATH = os.path.join(ROOTDIR, 'resources/font/Gabriola.ttf')

HOLE_POSITIONS = [(90, -20), (405, -20), (720, -20), (90, 140), (405, 140), (720, 140), (90, 290), (405, 290), (720, 290)]
BROWN = (150, 75, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
