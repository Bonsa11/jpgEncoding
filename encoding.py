import cv2
import numpy as np

from pre_processing import pre_process
from block_transforms import break_into_blocks, block_transform
from huffman import Node, huffman_encoding

# read uncompressed pixel data in
def read_image(path: str) -> np.array:
    """Read image data as numpy array"""

    return np.array(cv2.imread(path))


def encode_img(path: str, quality: int = 75):
    """Encoding portion of JPG"""

    # not sure how this is derived
    quant_array = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                            [12, 12, 14, 19, 26, 58, 60, 55],
                            [14, 13, 16, 24, 40, 57, 69, 56],
                            [14, 17, 22, 29, 51, 87, 80, 62],
                            [18, 22, 37, 56, 68, 109, 103, 77],
                            [24, 35, 55, 64, 81, 104, 113, 92],
                            [49, 64, 78, 87, 103, 121, 120, 101],
                            [72, 92, 95, 98, 112, 100, 103, 99]])

    raw_img = read_image(path)
    layers = []
    for img in pre_process(raw_img):
        blocks = list(break_into_blocks(img))
        for index, block in enumerate(blocks):
            new_block = block_transform(block, quant_array, quality)
            codes, encoded_block = huffman_encoding(new_block)
            blocks[index] = [codes, encoded_block]

        layers.append(blocks)
    return layers