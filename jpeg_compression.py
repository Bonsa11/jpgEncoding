"""Image Compression based on https://www.whydomath.org/node/wavlets/basicjpg.html"""
from encoding import encode_img
from decoding import decode_img


if __name__ == '__main__':
    print(encode_img('./data/voronoi_sphere.png', 60)[0][0])

