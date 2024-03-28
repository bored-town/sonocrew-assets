from pprint import pprint as pp
from PIL import Image
import os

src_path = './wonderland2024.csv'
out_dir  = './out'

# load raw data from csv
header = [ 'body', 'head', 'mask', 'mouth', 'accessorie', 'pet', 'front-distance' ]
raw = [ line.strip().split(',')[3:] for line in open(src_path, 'r') ][1:]

# craft to chars
chars = []
for r in raw:
    o = {}
    for (i, h) in enumerate(header):
        v = r[i] or None
        if (h == 'mask') and (v == 'white'):
            v = None
        o[h] = v
    chars.append(o)

# render char
trait_order = [ 'body', 'head', 'mask', 'accessorie', 'mouth', 'front-distance', 'pet' ]
gif_list = set()
for (idx, char) in enumerate(chars):
    no = idx + 1
    out_path = '{}/{}.png'.format(out_dir, no)
    new_img = Image.new("RGBA", (2000, 2000), "white")

    for t in trait_order:
        if char[t] is None:
            continue

        ext = 'jpg' if t == 'body' else 'png'
        trait_path = '../traits/{}/{}.{}'.format(t, char[t], ext)

        if not os.path.exists(trait_path):
            print('missing..', trait_path)
            gif_list.add(out_path)
            continue

        layer = Image.open(trait_path)
        if layer.mode != "RGBA":
            layer = layer.convert("RGBA")
        new_img = Image.alpha_composite(new_img, layer)

    if out_path not in gif_list:
        print('{}..'.format(out_path))
        new_img.save(out_path, "PNG")

# show skip files
print('skip GIF files:')
pp(gif_list)
