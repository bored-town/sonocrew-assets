from pprint import pprint as pp
from PIL import Image

out_path  = './out/{}.gif'

header = [ 'body', 'head', 'mask', 'mouth', 'accessorie', 'pet', 'front-distance' ]
trait_order = [ 'body', 'head', 'mask', 'accessorie', 'mouth', 'front-distance', 'pet' ]

render_list = [
    (6,  'mask', [ 'sexyalice.jpg', 'alice.png', ('DarkPatternAni', 8), 'fish_g.png', 'mask.png', 'Caterpillar.png', None ]),
    (7,  'mask', [ 'DarkQueen.jpg', 'chopped blue.png', ('DarkPatternAni', 8), None, None, None, None ]),
    (11, 'mask', [ 'SexyQueenofHeart.jpg', 'BlackQueen.png', ('blackani', 6), 'shy.png', None, None, None ]),
]

def load_img(src):
    img = Image.open(src)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    return img

def gen_gif_mask(token_id, raw):
    gen_gif(token_id, raw, 2, 2)

def gen_gif_mouth(token_id, raw):
    gen_gif(token_id, raw, 3, 4)

def gen_gif(token_id, raw, raw_idx, ord_idx):

    # prepare info
    gif_frames = []
    (key, time) = raw[raw_idx]
    char = dict(zip(header, raw))

    for frame_no in range(1, time+1):
        frame_path = '../traits/{}/{}/{:02}.png'.format(header[raw_idx], key, frame_no)

        # craft frame
        new_img = Image.new("RGBA", (2000, 2000), "white")
        for (i, t) in enumerate(trait_order):
            if char[t] is None:
                continue

            trait_path = frame_path if i == ord_idx else '../traits/{}/{}'.format(t, char[t])
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
for (token_id, mode, raw) in render_list:
    if mode == 'mask':
        gen_gif_mask(token_id, raw)
    elif mode == 'mouth':
        gen_gif_mouth(token_id, raw)
