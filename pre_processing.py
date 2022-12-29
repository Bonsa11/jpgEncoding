import numpy as np
from skimage.transform import downscale_local_mean

# convert data from RGB to YCbCr
def convert_rgb_ycbcr(img: np.array) -> np.array:
    """Convert RGB into YCbCr values"""

    print(f'png has shape {img.shape}')

    xform = np.array([[.299, .587, .114],
                      [-.1687, -.3313, .5],
                      [.5, -.4187, -.0813]
                    ])
    
    ycbcr = img.dot(xform.T)

    print(f'img has shape {ycbcr.shape}')

    return np.uint8(ycbcr)

def pad_array(arr, n):
    """add padding to 2D array"""
    w,h = arr.shape

    h_pad = 8-h%n
    w_pad = 8-w%n

    result = np.zeros((w+w_pad, h+h_pad))
    result[:w,:h] = arr

    return result


def pre_process_y_array(arr: np.array, n: int = 8) -> np.array:

    arr = pad_array(arr, n)
    arr -= 127

    return arr

def pre_process_c_array(arr: np.array, n: int = 8) -> np.array:
    """add padding to 2D array"""

    arr = down_scale(arr)
    arr = pad_array(arr, n)

    return arr


def down_scale(arr: np.array, scale_fac: float = 4) -> np.array:
    """Down scale 2D array"""
    return downscale_local_mean(arr, (scale_fac, scale_fac))


def pre_process(img: np.array):
    ycbcr = convert_rgb_ycbcr(img)

    y_arr = pre_process_y_array(ycbcr[:,:,0])
    cb_arr = pre_process_c_array(ycbcr[:,:,1])
    cr_arr = pre_process_c_array(ycbcr[:,:,2])

    print(f'y_arr has shape {y_arr.shape}')
    print(f'cb_arr has shape {cb_arr.shape}')
    print(f'cr_arr has shape {cr_arr.shape}')

    return [y_arr, cb_arr, cr_arr]



