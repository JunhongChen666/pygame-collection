import os



SCREENSIZE = (956, 560)

FONTPATH=None
# FONTPATH = os.path.join(os.getcwd(), 'resources/font/font.ttf')

IMAGEPATHS = {
    'asteroid': os.path.join(os.getcwd(), 'resources/images/asteroid.png'),
    # 'bg_big': os.path.join(os.getcwd(), 'resources/images/bg_big.png'),
    'bullet': os.path.join(os.getcwd(), 'resources/images/bullet.png'),
    'seamless_space': os.path.join(os.getcwd(), 'resources/images/seamless_space.png'),
    'red_ship': os.path.join(os.getcwd(), 'resources/images/playerShip1_red.png'),
    'blue_ship': os.path.join(os.getcwd(), 'resources/images/playerShip2_blue.png'),
    'ship_exploded': os.path.join(os.getcwd(), 'resources/images/ship_exploded.png'),
    # 'space3': os.path.join(os.getcwd(), 'resources/images/space3.jpg'),
}

SOUNDPATHS = {
    # 'boom': os.path.join(os.getcwd(), 'resources/sounds/boom.wav'),
    # 'Cool Space Music': os.path.join(os.getcwd(), 'resources/sounds/Cool Space Music.mp3'),
    # 'shot': os.path.join(os.getcwd(), 'resources/sounds/shot.ogg'),
}