import os
from os.path import join

import jinja2
import numpy as np
from PIL import Image

from model import Frame, Animation, Settings

ANIMATIONS_DIR = "animations"
TARGET_FILE = "animations.ino"

SETTINGS_FILE = "settings.json"
IMAGE_FILE_EXTS = (".png",)


def _transform(img: Image):
    arr = np.asarray(img)[:, :, :3]  # slice away transparency
    arr = arr.reshape((-1, 3))  # flatten

    #                      target ranges              previous range
    quantized_arr = arr * [2 ** 3, 2 ** 3, 2 ** 2] // 2 ** 8

    triples = []
    for triple in quantized_arr:
        triples.append(str(np.sum(triple * [2 ** 5, 2 ** 2, 1])))

    return triples


def load_animations():
    animations = []

    for i, animation_name in enumerate(sorted(os.listdir(ANIMATIONS_DIR))):
        animation_dir = join(ANIMATIONS_DIR, animation_name)

        frames = []
        for frame_name in filter(lambda f: f.endswith(IMAGE_FILE_EXTS), sorted(os.listdir(animation_dir))):
            frame_path = join(animation_dir, frame_name)
            img = Image.open(frame_path)

            transformed = _transform(img)

            frames.append(Frame(transformed))

        settings = Settings(join(animation_dir, SETTINGS_FILE))
        animations.append(Animation(f"{i:03d}", animation_name, frames, settings))

    return animations


def compile_animations(animations):
    template = jinja2.Environment(loader=jinja2.FileSystemLoader(".")).get_template("animations.ino.template")
    output = template.render(animations=animations,
                             frameCounts=[len(anim.frames) for anim in animations],
                             speeds=[anim.settings.speed for anim in animations])

    with open(TARGET_FILE, "w") as f:
        f.write(output)


def main():
    animations = load_animations()
    compile_animations(animations)


if __name__ == '__main__':
    main()