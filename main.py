from PIL import Image
import numpy as np
import os

def import_dataset():
    shapes = ["circle", "square", "triangle", "star"]
    dataset = {}

    for shape in shapes:
        shape_dir = f"shapes/{shape}"
        dataset[shape] = [np.asarray(Image.open(f"{shape_dir}/{image}")) for image in os.listdir(shape_dir)]

    return dataset


dataset = import_dataset()