import numpy as np
from typing import List
from scipy.fftpack import dct

def discrete_cos_transform(img: np.array) -> np.array:
    """2D Discrete COsine TRansform on Matrix"""
    # will do this myself at some point in the future
    return dct(dct(img.T, norm='ortho').T, norm='ortho')


def quantization(img: np.array, quant_array: np.array, quality: int = 75) -> np.array:
    """Quantization of cosine transfomred matrix"""

    if quality < 50:
        s = 5000/quality
    else:
        s = 200 - 2*quality

    Ts = (s*quant_array + 50) // 100

    Ts[Ts == 0] = 1

    return np.divide(img, Ts)


def block_transform(block: np.array, quant_array: np.array, quality: int = 75):
    cos_block = discrete_cos_transform(block)
    return quantization(cos_block, quant_array, quality).astype(int)


# break into nxn blocks and process
def break_into_blocks(img: np.array, n: int = 8) -> List[np.array]:
    """Break np.array into multiple nxn pixel blocks"""
    return (img.reshape(1, n, -1, n)
               .swapaxes(1,2)
               .reshape(-1, n, n))