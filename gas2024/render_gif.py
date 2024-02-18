# TODO craft ani-mask
# TODO craft custom (body + mask)

from pprint import pprint as pp
from PIL import Image

out_path  = './out/{}.gif'

header = [ 'body', 'head', 'mask', 'mouth', 'accessorie', 'pet', 'front-distance' ]
trait_order = [ 'body', 'head', 'mask', 'accessorie', 'mouth', 'front-distance', 'pet' ]

no_2 = [ 'Huntergang.jpg', 'bloodgang.png', None, ('ani-laugh', 11), 'tattoo.png', None, None ]
no_4 = [ 'deathgang.jpg', 'huntergang.png', ('blackanimate', 4), 'pierce-tounge.png', None, 'ghost.png', None ]
no_6 = [ 'killgang.jpg', 'biggang.png', 'goldmask.png', ('ani-laugh', 11), 'mask.png', None, None ]
no_9 = [ 'bloodgang.jpg', 'birdnestblue.png', ('blackanimate', 4), 'money.png', 'tattoo.png', None, None ]
no_10 = [ 'Hebisnake.jpg', 'GalsGangblue.png', ('blackani', 6), 'flower.png', None, None, None ]
no_11 = [ 'firegang.jpg', 'Galsgang.png', ('firemaskani', 6), 'yummy.png', 'heart.png', None, None ]
no_14 = [ 'prettygang.jpg', 'catear.png', ('firemaskani', 6), 'sharp.png', 'teeth.png', 'star.png', None, None ]
no_17 = [ 'beatgang.jpg', 'prettygang.png', ('blackani', 6), 'pierce-mouth.png', None, None, None ]
no_20 = [ 'Hebigang.jpg', 'green china.png', ('blackani', 6), 'cigarette.png', None, None, None ]
no_25 = [ 'Galsgang.jpg', 'grey pigtail.png', ('blackani', 6), 'flower.png', 'star.png', None, None ]

def load_img(src):
    img = Image.open(src)
    if img.mode != "RGBA":
        img = img.convert("RGBA")
    return img

# TODO craft ani-mouth
token_id = 2
raw = no_2
raw_idx = 3
ord_idx = 4

gif_frames = []
(key, time) = raw[raw_idx]
char = dict(zip(header, raw))
for frame_no in range(1, time+1):
    frame_path = '../traits/{}/{}/{:02}{}.png'.format(header[raw_idx], key, frame_no, key)

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

gif_path = out_path.format(token_id)
gif_frames[0].save(gif_path, save_all=True, append_images=gif_frames[1:], loop=0, duration=150)

print(gif_path)

"""
no = idx + 1
out_path = '{}/{}.png'.format(out_dir, no)
new_img = Image.new("RGBA", (2000, 2000), "white")

for t in trait_order:
    if char[t] is None:
        continue

    ext = 'jpg' if t == 'body' else 'png'
    trait_path = '../traits/{}/{}.{}'.format(t, char[t], ext)

    if not os.path.exists(trait_path):
        gif_list.add(out_path)
        continue

    layer = Image.open(trait_path)
    if layer.mode != "RGBA":
        layer = layer.convert("RGBA")
    new_img = Image.alpha_composite(new_img, layer)

if out_path not in gif_list:
    print('{}..'.format(out_path))
    new_img.save(out_path, "PNG")
"""

"""
modified_frames = []
for (idx, mouth) in enumerate(mouth_frames):
    
    # Create a copy of the frame
    new_frame = bg_img.copy()
    mask = mask_frames[idx]

    if mouth.mode != "RGBA":
        mouth = mouth.convert("RGBA")
    if mask.mode != "RGBA":
        mask = mask.convert("RGBA")

    new_frame = Image.alpha_composite(new_frame, mouth)
    new_frame = Image.alpha_composite(new_frame, mask)
    #new_frame.paste(mouth, (0, 0), mouth)
    #new_frame.paste(mask, (0, 0), mask)

    # Append the modified frame to the list
    modified_frames.append(new_frame)

# Save the modified frames as a new GIF
modified_frames[0].save("merged_image.gif", save_all=True, append_images=modified_frames[1:], loop=0, duration=150)
"""
