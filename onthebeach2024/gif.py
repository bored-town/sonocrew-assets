import sys
sys.path.append('../')
from render_gif import *

render_list = [
    (1,  'mouth', [ 'Cloud-Dress.jpg', 'flowerhead.png', 'black_g.png', ('Ani-Fish', 7), None, None, None ]),
    (2,  'mouth', [ 'green tank top.jpg', 'Thaigreen.png', None, ('Pipe', 6), None, None, None ]),
    (8,  'custom',[ 'beach-tank-top.jpg', 'SailorHat.png', None, ('Pipe', 6), None, ('SeaGull', 4), None ]),
    (10, 'pet',   [ 'leopard-bikini.jpg', 'catear.png', None, 'shy.png', None, ('SeaGull', 4), None ]),
    (12, 'mouth', [ 'Shellbikini.jpg', 'rainbow-curly.png', None, ('Ani-Fish', 7), 'heart.png', None, None ]),
    (13, 'pet',   [ 'swimwarmflower.jpg', 'coconuthead.png', 'leaf_g.png', 'smile_g.png', None, ('SeaGull', 4), None ]),
]

def gen_gif_no_8(token_id=8, raw=render_list[2][2]):

    # prepare info
    gif_frames = []
    time = 12 # frames
    char = dict(zip(header, raw))

    for frame_no in range(1, time+1):
        mouth_path = '../traits/mouth/Pipe/{:02}.png'.format(calc_gif_frame(frame_no, 6))
        pet_path = '../traits/pet/SeaGull/{:02}.png'.format(calc_gif_frame(frame_no, 4))

        # craft frame
        new_img = Image.new("RGBA", (2000, 2000), "white")
        for (i, t) in enumerate(trait_order):
            if char[t] is None:
                continue

            trait_path = '../traits/{}/{}'.format(t, char[t])
            if i == 4:
                trait_path = mouth_path
            elif i == 6:
                trait_path = pet_path
            layer = Image.open(trait_path)

            if layer.mode != "RGBA":
                layer = layer.convert("RGBA")
            new_img = Image.alpha_composite(new_img, layer)

        gif_frames.append(new_img)

    # save gif
    gif_path = out_path.format(token_id)
    gif_frames[0].save(gif_path, save_all=True, append_images=gif_frames[1:], loop=0, duration=150)
    print(gif_path)

# render gif
gen_gif_from_list(render_list)

# render gif (custom)
gen_gif_no_8()
