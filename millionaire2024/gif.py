import sys
sys.path.append('../')
from render_gif import *

wink = ('wink', 5)
render_list = [
    (1,  'front-distance', [ 'blink-suit.jpg', 'fujingang.png', 'fujinmask.png', None, None, None, wink]),
    (4,  'front-distance', [ 'white-gold-dress.jpg', 'gold-headband.png', None, 'flower.png', None, 'Money-Cat.png', wink]),
    (8,  'front-distance', [ 'dollar-shirt.jpg', 'diamond-hair.png', None, 'sharp teeth.png', None, 'leprechaun.png', wink]),
    (12, 'front-distance', [ 'white-fur.jpg', 'legendred.png', 'robot.png', 'zigar.png', None, None, wink]),
    (16, 'front-distance', [ 'goldchainsuit.jpg', 'curly blond.png', None, None, 'cyborg.png', None, wink]),
    (19, 'front-distance', [ 'dollar-suit.jpg', 'horsehead.png', None, None, None, None, wink]),
]

# render gif
out_path = sys.argv[1] + '/{}.gif'
gen_gif_from_list(render_list, out_path)
